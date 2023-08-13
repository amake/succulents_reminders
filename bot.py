import os
from contextlib import contextmanager
from io import BytesIO
from mastodon import Mastodon
from configparser import ConfigParser
from datetime import date
import succs

config_file = 'config.ini'


def load_config():
    if not os.path.isfile(config_file):
        print('No credentials file found. Please create one.')
        exit(1)
    c = ConfigParser()
    c.read(config_file)
    return c


config = load_config()

mastodon = Mastodon(client_id='bot_clientcred.secret',)
mastodon.log_in(
    config['Auth']['username'],
    config['Auth']['password'],
)


def choose_tip():
    today = date.today()
    tips = succs.get_tips(today, succs.Hemisphere.Northern)
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


def post(tip: succs.Tip):
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
    tip = choose_tip()
    if tip:
        post(tip)
    else:
        print('No tips found for today.')
