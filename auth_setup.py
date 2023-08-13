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

for flavor in bot.Flavor:
    secret_file = f'{flavor}_clientcred.secret'

    if os.path.isfile(secret_file):
        print(f'Secret file for {flavor} already exists. Skipping.')
        continue

    Mastodon.create_app(
        config[flavor]['app_name'],
        api_base_url=config[flavor]['api_base_url'],
        to_file=secret_file
    )

print('Done')
