from flask_login import UserMixin
from . import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    books = db.relationship('Book')


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10000))
    read = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))