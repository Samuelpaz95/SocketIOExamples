from app import init_app
from config import config

app, socketio = init_app(config=config['dev'])
if __name__ == '__main__':
    socketio.run(app)
    