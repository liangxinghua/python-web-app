# -*- coding:utf-8 -*-

from app import db

ROLE_USER = 0
ROLE_ADMIN = 1


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    role = db.Column(db.SmallInteger, default=ROLE_USER)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    # 是否可认证
    def is_authenticated(self):
        return True

    # 是否激活
    def is_active(self):
        return True

    # 是否为僞造用户
    def is_anonymous(self):
        return False

    # 唯一标识
    def get_id(self):
        return unicode(self.id)

    @classmethod
    def login_check(cls, user_name):
        user = cls.query.filter(
            db.or_(User.nickname == user_name,
                   User.email == user_name)
        ).first()

        if not user:
            return None
        return user

    def __repr__(self):
        return '<User %r>' % (self.nickname)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), index=True)
    body = db.Column(db.String(5000))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)
