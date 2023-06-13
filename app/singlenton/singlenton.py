from flask import Flask
from flask_socketio import SocketIO

APP = Flask('app')
SOCKETIO = SocketIO(cors_allowed_origins='*', async_mode='eventlet')

def get_socketio():
    return SOCKETIO

def get_app():
    return APP