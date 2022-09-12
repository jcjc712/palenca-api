from __future__ import annotations
from typing import Dict
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from src.blueprints.core.domain import model


def add_user(data: Dict[str, str], session=None):
    user = session.query(model.User).get(data['email'])
    if user is not None:
        raise RegisterException

    hashed_password = generate_password_hash(data["password"])
    session.add(model.User(email=data["email"], password=hashed_password))
    session.commit()


class LoginException(Exception):
    pass


class RegisterException(Exception):
    pass


def profile(
        email: str, session=None
):
    user = session.query(model.User).get(email)
    return {
        "platform": "uber",
        "profile":{
       "country": "mx",
       "city_name": "Ciudad de Mexico",
       "worker_id": "34dc0c89b16fd170eba320ab186d08ed",
       "first_name": "Pierre",
       "last_name": "Delarroqua",
       "email": user.email,
       "phone_prefix": "+52",
       "phone_number": "5576955981",
       "rating": "4.8",
       "lifetime_trips": 1254
   }}


def login(
        data: Dict[str, str], session=None
):
    user = session.query(model.User).get(data['email'])
    if user is not None and check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity=data['email'])
        return access_token
    else:
        raise LoginException
