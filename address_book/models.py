from datetime import datetime

from flask_login import UserMixin
from sqlalchemy import Sequence
from werkzeug.security import generate_password_hash, check_password_hash

from .components import db, login


@login.user_loader
def load_user(id):
    return User.query.get(id)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, Sequence('user_id_seq'), primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    contacts = db.relationship('Contact', backref='author', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_contacts(self, **kwargs):
        contacts = Contact.query.filter_by(user_id=self.id, **kwargs)
        return contacts

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def __init__(self, username, email):
        self.username = username
        self.email = email


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    name = db.Column(db.String(30))
    surname = db.Column(db.String(50))
    email = db.Column(db.String(30))
    phone = db.Column(db.String(15))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def get_user(self):
        user = User.query.get(self.user_id)
        return user

    def __repr__(self):
        return '<Contact {}{}>'.format(self.name, self.surname)

    def as_dict(self):
        return {"id": self.id, "name": self.name, "surname": self.surname, "email": self.email, "phone": self.phone}
