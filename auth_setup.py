import os
from configparser import ConfigParser
from mastodon import Mastodon

secret_file = 'bot_clientcred.secret'

if os.path.isfile(secret_file):
    print('Secret file already exists. Nothing to do.')
    exit(0)

config_file = 'config.ini'


def load_config():
    if not os.path.isfile(config_file):
        print('No credentials file found. Please create one.')
        exit(1)
    c = ConfigParser()
    c.read(config_file)
    return c


config = load_config()

Mastodon.create_app(
    config['App']['app_name'],
    api_base_url=config['App']['api_base_url'],
    to_file=secret_file
)

print('Done')
