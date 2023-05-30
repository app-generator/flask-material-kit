# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_login import UserMixin

from apps import db, login_manager

from apps.authentication.util import hash_pass
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.schema import Index
from sqlalchemy.sql.expression import func

class Users(db.Model, UserMixin):

    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.LargeBinary)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]

            if property == 'password':
                value = hash_pass(value)  # we need bytes here (not plain str)

            setattr(self, property, value)

    def __repr__(self):
        return str(self.username)
    
class User:
    def __init__(self, username):
        self.username = username

@login_manager.user_loader
def user_loader(id):
    return Users.query.filter_by(id=id).first()

@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    user = Users.query.filter_by(username=username).first()
    return user if user else None

class Resources(db.Model):

    __tablename__ = 'resources'

    topic_group = db.Column(db.Integer)
    topic_title = db.Column(db.String(80))
    subtopic1 = db.Column(db.String(80))
    subtopic2 = db.Column(db.String(80))
    subtopic3 = db.Column(db.String(80))
    subtopic4 = db.Column(db.String(80))
    subtopic5 = db.Column(db.String(80))
    subtopic6 = db.Column(db.String(80))
    subtopic7 = db.Column(db.String(80))
    subtopic8 = db.Column(db.String(80))
    title = db.Column(db.Text, primary_key=True)
    author = db.Column(db.String(20), unique=True)
    author2 = db.Column(db.String(20), unique=True)
    website = db.Column(db.Text, unique=True)


class Post(db.Model):
    __searchable__=['title','topic_group','subtopic1','subtopic2','subtopic3','subtopic4','subtopic5','subtopic6','subtopic7','subtopic8']

    topic_group = db.Column(db.Integer)
    topic_title = db.Column(db.String(80))
    subtopic1 = db.Column(db.String(80))
    subtopic2 = db.Column(db.String(80))
    subtopic3 = db.Column(db.String(80))
    subtopic4 = db.Column(db.String(80))
    subtopic5 = db.Column(db.String(80))
    subtopic6 = db.Column(db.String(80))
    subtopic7 = db.Column(db.String(80))
    subtopic8 = db.Column(db.String(80))
    title = db.Column(db.Text, primary_key=True)
    author = db.Column(db.String(20), unique=True)
    author2 = db.Column(db.String(20), unique=True)
    website = db.Column(db.Text, unique=True)