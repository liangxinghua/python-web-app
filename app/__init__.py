# -*- coding:utf-8 -*-

from flask import Blueprint

front = Blueprint(__name__, "app", static_folder="static", template_folder="templates",static_url_path="/app/static")

from app import models, views, forms
