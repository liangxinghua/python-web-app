# -*- coding:utf-8 -*-

from flask import render_template, make_response
from admin import admin
from models import Article


@admin.app_errorhandler(404)
def page_not_found(error):
    resp = make_response(render_template("admin/404.html"), 404)
    resp.headers["X-somthing"] = error
    return resp


@admin.route("/", methods=["GET", "POST"])
def index():
    return render_template("admin/index.html")


@admin.route("/article/", methods=["GET", "POST"])
def art_list():
    return render_template("admin/about.html")


@admin.route("/article/publish", methods=["GET", "POST"])
def art_publish():
    return render_template("admin/article/publish.html")
