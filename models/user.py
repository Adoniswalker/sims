from werkzeug.security import generate_password_hash

from main import db


class Saving(object):

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self


class User(db.Model, Saving):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(600), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password =  generate_password_hash(password)

    def __repr__(self):
        return '<User %r>' % self.username
