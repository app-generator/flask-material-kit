# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# from flask_login import UserMixin

# from apps import db, login_manager

# from apps.authentication.util import hash_pass
# from sqlalchemy.ext.declarative import declared_attr
# from sqlalchemy.schema import Index
# from sqlalchemy.sql.expression import func


# class Resources(db.Model):

#     __tablename__ = 'resources'

#     topic_group = db.Column(db.Integer)
#     topic_title = db.Column(db.String(80))
#     subtopic1 = db.Column(db.String(80))
#     subtopic2 = db.Column(db.String(80))
#     subtopic3 = db.Column(db.String(80))
#     subtopic4 = db.Column(db.String(80))
#     subtopic5 = db.Column(db.String(80))
#     subtopic6 = db.Column(db.String(80))
#     subtopic7 = db.Column(db.String(80))
#     subtopic8 = db.Column(db.String(80))
#     title = db.Column(db.Text, primary_key=True)
#     author = db.Column(db.String(20), unique=True)
#     author2 = db.Column(db.String(20), unique=True)
#     website = db.Column(db.Text, unique=True)


# class Post(db.Model):
#     __searchable__=['title','topic_group','subtopic1','subtopic2','subtopic3','subtopic4','subtopic5','subtopic6','subtopic7','subtopic8']

#     topic_group = db.Column(db.Integer)
#     topic_title = db.Column(db.String(80))
#     subtopic1 = db.Column(db.String(80))
#     subtopic2 = db.Column(db.String(80))
#     subtopic3 = db.Column(db.String(80))
#     subtopic4 = db.Column(db.String(80))
#     subtopic5 = db.Column(db.String(80))
#     subtopic6 = db.Column(db.String(80))
#     subtopic7 = db.Column(db.String(80))
#     subtopic8 = db.Column(db.String(80))
#     title = db.Column(db.Text, primary_key=True)
#     author = db.Column(db.String(20), unique=True)
#     author2 = db.Column(db.String(20), unique=True)
#     website = db.Column(db.Text, unique=True)