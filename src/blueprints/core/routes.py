from flask import Blueprint, jsonify
from src.blueprints.core.service_layer import handlers
from src.extension import db
from flask_jwt_extended import jwt_required, get_jwt_identity

from flask import request
import re
main_page = Blueprint('main_page', __name__)


def validation(email: str, password: str):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise ValueError("Invalid email")
    if len(password) < 5:
        raise ValueError("Invalid password")


@main_page.route('/', methods=['GET'])
def index():
    return "Hello Palenca"


@main_page.route('/uber/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    try:
        validation(email, password)
        access_token = handlers.login({"email": email, "password": password}, session=db.session)
        return jsonify(message='success', access_token=access_token), 200
    except ValueError as e:
        return jsonify(message=str(e)), 401
    except handlers.LoginException:
        return jsonify(message='CREDENTIALS_INVALID'), 401


@main_page.route('/uber/profile', methods=['GET'])
@jwt_required()
def profile():
    result = handlers.profile(get_jwt_identity(), session=db.session)
    result.update({"message": "SUCCESS"})
    return jsonify(result), 200


@main_page.route('/uber/register', methods=["POST"])
def register():
    email = request.json.get('email')
    password = request.json.get('password')
    try:
        validation(email, password)
        handlers.add_user({"email": email, "password": password}, session=db.session)
        return jsonify(message='SUCCESS'), 201
    except ValueError as e:
        return jsonify(message=str(e)), 401
    except handlers.RegisterException:
        return jsonify(message='REGISTER_INVALID'), 401
