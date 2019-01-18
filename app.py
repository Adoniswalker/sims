from marshmallow import Schema, fields, post_load
from flask import jsonify
from main import app
from models import User

class UserSchema(Schema):
    id = fields.Int()
    email = fields.Email()
    username = fields.String()

    @post_load
    def create_user(self, data):
        return User(**data)


user = User.query.all()
schema = UserSchema(many=True)


@app.route('/')
def hello_world():
    return jsonify(schema.dump(user))
