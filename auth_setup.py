import os
from configparser import ConfigParser
from mastodon import Mastodon
import bot


def load_config(config_file):
    if not os.path.isfile(config_file):
        print('No config file found. Please create one.')
        exit(1)
    c = ConfigParser()
    c.read(config_file)
    return c


config = load_config('config.ini')

scopes = ['write:media', 'write:statuses']

for flavor in bot.Flavor:
    secret_file = f'{flavor}_clientcred.secret'

    if os.path.isfile(secret_file):
        print(f'Secret file for {flavor} already exists. Skipping.')
        continue

    Mastodon.create_app(
        config[flavor]['app_name'],
        api_base_url=config[flavor]['api_base_url'],
        scopes=scopes,
        to_file=secret_file
    )

    mastodon = Mastodon(client_id=secret_file)
    print('Visit the URL below and enter the code.')
    print(mastodon.auth_request_url(scopes=scopes))
    code = input('Code: ')
    mastodon.log_in(
        to_file=f'{flavor}_usercred.secret',
        code=code,
        scopes=scopes
    )

print('Done')
