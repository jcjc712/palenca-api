from __future__ import annotations
from src.extension import db
from sqlalchemy.sql import func


# class ExchangeRate(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     currency = db.Column(db.String(100), nullable=False)
#     mx_amount = db.Column(db.String(100), nullable=False)
#     created_at = db.Column(db.DateTime(timezone=True),
#                            server_default=func.now())

class User(db.Model):
    email = db.Column(db.String(100), nullable=False, primary_key=True)
    # platform = db.Column(db.String(100), nullable=False)
    # country = db.Column(db.String(100), nullable=False)
    # city_name = db.Column(db.String(100), nullable=False)
    # worker_id = db.Column(db.String(100), nullable=False)
    # first_name = db.Column(db.String(100), nullable=False)
    # last_name = db.Column(db.String(100), nullable=False)
    # phone_prefix = db.Column(db.String(100), nullable=False)
    # phone_number = db.Column(db.String(100), nullable=False)
    # rating = db.Column(db.String(2), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    # lifetime_trips = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    def __repr__(self):
        return f'<User {self.email}>'
