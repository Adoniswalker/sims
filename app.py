from marshmallow import Schema, fields, post_load
from flask import jsonify
from models import User
# from main import create_app

# app = create_app()
# app.app_context().push()
from main import app


class UserSchema(Schema):
    id = fields.Int()
    email = fields.Email()
    username = fields.String()

    @post_load
    def create_user(self, data):
        return User(**data)


# def do_math():
# with app.app_context():
user = User.query.all()
schema = UserSchema(many=True)
# return schema.dump(user)

@app.route('/')
def hello_world():
    return jsonify(schema.dump(user))
