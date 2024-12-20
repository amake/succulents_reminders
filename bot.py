import os
from contextlib import contextmanager
from io import BytesIO
from mastodon import Mastodon
from configparser import ConfigParser
import datetime
from enum import StrEnum
import succs


def load_config(config_file):
    if not os.path.isfile(config_file):
        print('No config file found. Please create one.')
        exit(1)
    c = ConfigParser()
    c.read(config_file)
    return c


config = load_config('config.ini')


class Flavor(StrEnum):
    """Flavor of the bot."""

    North = 'North'
    South = 'South'


def get_client(flavor: Flavor):
    mastodon = Mastodon(access_token=f'{flavor}_usercred.secret')
    return mastodon


def choose_tip(flavor: Flavor, date: datetime.date):
    tips = succs.get_tips(
        date,
        succs.Hemisphere.Northern if flavor == Flavor.North
        else succs.Hemisphere.Southern
    )
    return tips[0] if tips else None


@contextmanager
def s3_file(bucket: str, path: str):
    import boto3
    s3 = boto3.client('s3')
    file_bytes = BytesIO()
    try:
        s3.download_fileobj(bucket, path, file_bytes)
        file_bytes.seek(0)
        yield file_bytes
    finally:
        file_bytes.close()


def post(flavor: Flavor, tip: succs.Tip):
    mastodon = get_client(flavor)

    images = succs.get_images(tip)

    media_dicts = []
    for image in images:
        with s3_file('amake-bots', f'succs/{image}') as img_file:
            media_dict = mastodon.media_post(img_file, mime_type='image/jpg')
            media_dicts.append(media_dict)

    mastodon.status_post(
        succs.format_tip(tip),
        media_ids=[media_dict['id'] for media_dict in media_dicts],
        visibility='public',
        language='en'
    )


def do_toot(event, context):
    date = None
    try:
        date = datetime.datetime.strptime(event['date'], '%Y-%m-%d')
    except Exception:
        pass
    date = date or datetime.date.today()
    for flavor in Flavor:
        if tip := choose_tip(flavor, date):
            print(f'Posting for {flavor}: {tip}...', end=None)
            try:
                post(flavor, tip)
                print('Succcess')
            except Exception as e:
                print(f'Failed to post for {flavor}: {e}')
        else:
            print(f'No tips found for {flavor} on {date}.')
