import logging
from flask import Blueprint
from flask import render_template
from flask_socketio import emit, join_room, send
from ..singlenton import get_socketio, get_app

page = Blueprint('page', __name__)
socketio = get_socketio()
app = get_app()

@page.route('/', methods=['GET'])
def index():
    return render_template('index.html', title='sockets')


@socketio.on('connect')
def connect():
    app.logger.info('client connected!')
    print ('-------------------conncected!!!-------------------')

@socketio.on('disconnect')
def disconnect():
    app.logger.info('client connected!')
    print ('-------------------disconnected!!!-------------------')

@socketio.on('join')
def join(data):
    username = data.get('username')
    room = data.get('room')
    join_room(room)
    send(f'{username} has entered the room:', room=room)
    print (f'-------------------{username} se unio a {room}-------------------')

@socketio.on('new_message')
def new_message(data):
    room = data.get('room')
    emit('new_message', dict(data), broadcast=True, to=room)