# -*- coding:utf-8 -*-

from comm import db


class Article(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), index=True, unique=True)
    body = db.Column(db.String(5000))
    timestamp = db.Column(db.DateTime)
