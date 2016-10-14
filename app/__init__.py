# -*- coding:utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# 初始化flask 应用
app = Flask(__name__)
app.config.from_object("config")

# 初始化数据库
db = SQLAlchemy(app)

# 初始化登录
lm=LoginManager()
lm.setup_app(app)

from app import views, models
