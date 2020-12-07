import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

basedir = os.path.abspath(os.path.dirname(__file__))


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'project_name.db')}"
    app.config['SECRET_KEY'] = b'&f\x91vI\xe7\xb3\x93\xafk\xe7,\xebU`\x93'

    from .views import bp_main

    app.register_blueprint(bp_main)

    db.init_app(app)
    Migrate(app, db)

    return app
