from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


# def create_app():
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dennisngeno:testpassword@localhost/sims'
db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# migrate = Migrate(app, db)
# with app.app_context():
# db.init_app(app)
# return app
