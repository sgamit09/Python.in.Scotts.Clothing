from email.policy import default
from enum import unique
from time import timezone
from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

class Clothing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(10000))
    flaws = db.Column(db.String(10000))
    size = db.Column(db.String(10000))
    measurements = db.Column(db.String(10000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #one to many relationship

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')