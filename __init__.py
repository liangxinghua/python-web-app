# -*- coding:utf-8 -*-

from flask import Flask
from admin import admin
from app import front
from comm import db, lm


def create_app(config):
    app = Flask(__name__)

    app.config.from_object(config)

    # 注册蓝图
    app.register_blueprint(front)
    app.register_blueprint(admin)

    # 初始化数据库
    db.init_app(app)

    # 登录管理
    lm.init_app(app)

    return app

