from flask import Flask
from src.config import get_mysql_uri
import os
from src.extension import jwt, db


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = get_mysql_uri()
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', None)
    app.config["JWT_SECRET_KEY"] = os.environ.get('JWT_SECRET_KEY', None)

    jwt.init_app(app)
    db.init_app(app)

    from src.blueprints.core import bp as bp_core

    with app.app_context():
        db.create_all()
    bp_core.config(app)

    return app
