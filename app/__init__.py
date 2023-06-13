from .singlenton import get_app, get_socketio
from .api import page

app = get_app()
socketio = get_socketio()

def init_app(config):
    app.config.from_object(config)
    app.register_blueprint(page)
    socketio.init_app(app)
    return app, socketio

