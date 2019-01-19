import os

import pem
from flask import request
from flask_migrate import Migrate, MigrateCommand
from flask_restplus import Api, Resource
from github import Github
from marshmallow import ValidationError

from main import app, db
from schemas.user import UserSchema
from flask_script import Manager
from models.user import *

api = Api(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

user = User.query.all()
schema_get = UserSchema(many=True)
schema_post = UserSchema()


@api.route('/users')
class UsersView(Resource):
    def get(self):
        return schema_get.dump(user)

    def post(self):
        user_details = request.get_json()
        try:
            clean_data = schema_post.load(user_details)
            data = User(**clean_data)
            db_response = data.save()
            response = schema_post.dump(db_response)
            return {"data": response}, 200
        except ValidationError as err:
            errors = err.messages
            valid_data = err.valid_data
            return {"errors": errors, "valid": valid_data}, 400


@api.route("/github")
class GitHub(Resource):
    def get(self):
        certs = pem.parse_file("pullrequestslackbot.2019-01-19.private-key.pem")
        g = Github(str(certs[0]))
        g = Github(client_id=os.environ.get("CLIENT_ID"), client_secret=os.environ.get("CLIENT_SECRET"))
        f = g.get_user().get_repos()
        return [repo.name for repo in g.get_user().get_repos()]


if __name__ == "__main__":
    manager.run()
