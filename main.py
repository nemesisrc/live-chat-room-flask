from flask import Flask, render_template, url_for, request, redirect, jsonify, session
from flask_socketio import SocketIO, join_room, leave_room, send, emit
import random # for room codes
from string import ascii_uppercase
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
socketio = SocketIO(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        code = request.form.get('code')
        join = request.form.get('join', False)  # False is the default value to be returned if the key can't be looked up
        create = request.form.get('create', False)
    return render_template('home.html')


if __name__ == '__main__':
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True) # allow_unsafe_werkzeug=True is used for debugging purposes only, not recommended for production use