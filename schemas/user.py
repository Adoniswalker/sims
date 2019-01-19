from marshmallow import Schema, fields, validate, post_load
from werkzeug.security import generate_password_hash, check_password_hash

from validators.names_validators import email_validator, validate_username


class UserSchema(Schema):
    id = fields.Int(dump_only=True, validate=email_validator)
    email = fields.String(required=True, validate=(validate.Email(error="Not a valid address"), email_validator))
    username = fields.String(required=True, validate=(validate.Regexp("^(?=.{4,30}$)(?![_.])(?!.*[_.]{2})["
                                                                      "a-zA-Z0-9._]+(?<![_.])$",
                                                                      error="Invalid username"), validate_username))
    password = fields.String(required=True, load_only=True,
                             validate=validate.Regexp("^(?=.*\d).{8,20}$", error="Password must have "
                                                                                 "atleast and int and "
                                                                                 "have 8 characters"))

    # @post_load()
    # def set_password(self, data):
    #     self.password = generate_password_hash(data["password"])

    def check_password(self, data):
        return check_password_hash(self.pw_hash, data["password"])
