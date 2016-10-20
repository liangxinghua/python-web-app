# -*- coding:utf-8 -*-

from flask import Blueprint

admin = Blueprint("admin", __name__, static_folder="static", static_url_path="/admin/static",
                  template_folder="templates",
                  url_prefix="/admin")

from admin import views, models
