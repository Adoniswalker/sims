from marshmallow import ValidationError

from models.user import User


def email_validator(email):
    """
    Checks if given string is at least 1 character and only contains letters,
    numbers and non consecutive fullstops, hyphens, spaces and apostrophes.
    Raises validation error otherwise.
    """
    if User.query.filter(User.email == email).first():
        raise ValidationError("Email has been used")


def validate_username(username):
    if User.query.filter(User.username == username).first():
        raise ValidationError("Username already taken")