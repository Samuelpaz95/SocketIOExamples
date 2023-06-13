from logging import DEBUG
from flask import Config

class DevConfig(Config):
    DEBUG = True
    SECRET_KEY = 'thisIsASecretKey'
    SOCKETS_ALLOW_ORIGIN = ['*']

config = {
    'dev': DevConfig
}