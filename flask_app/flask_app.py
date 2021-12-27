from flask import Flask
from datetime import date
import json
from pathlib import Path
from flask_restful import Api, Resource, abort, reqparse
from hashlib import sha256
from uuid import uuid4

class JSONStorage:
    def __init__(self, filename):
        self._filename = Path(filename).resolve()
        if not self._filename.is_file():
            self.clear()

    def __setitem__(self, key, value):
        users = self._load()
        users[key] = value
        self._dump(users)

    def __getitem__(self, key):
        return self._load()[key]

    def __delitem__(self, key):
        users = self._load()
        del users[key]
        self._dump(users)

    def __contains__(self, item):
        return item in self._load()

    def clear(self):
        self._dump({})

    def _dump(self, obj):
        with open(self._filename, 'w') as file:
            json.dump(obj, file)

    def _load(self):
        with open(self._filename) as file:
            return json.load(file)

app = Flask(__name__)
api = Api(app)
users = JSONStorage('users.json')

user_args_parser = reqparse.RequestParser().add_argument(
    'password', type=str, help='Need a user password',
    required=True)

def if_user(username):
    if username in users:
        abort(409, message='!This username is already taken!')

def if_notuser(username):
    if username not in users:
        abort(404, message='!This username is not found!')

def paswd_hash(password):
    salt = uuid4().hex
    return salt + sha256((password + salt).encode()).hexdigest()

class User(Resource):

    def get(self, username):
        if_notuser(username)
        return users[username]

    def put(self, username):
        if_user(username)
        password = user_args_parser.parse_args()['password']
        today = date.today()
        current_date = today.strftime("%d/%m/%Y")
        users[username] = {
            'password': paswd_hash(password),
            'registrationDate':current_date
        }
        return users[username], 201

    def delete(self, username):
        if_notuser(username)
        del users[username]
        return '', 204
api.add_resource(User, '/user/<string:username>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7070)
