# -*- coding:utf-8 -*-

from flask import  render_template,make_response
from admin import admin


@admin.app_errorhandler(404)
def page_not_found(error):
    resp = make_response(render_template("admin/404.html"), 404)
    resp.headers["X-somthing"] = error
    return resp

@admin.route("/",methods=["GET","POST"])
def index():
    return render_template("admin/index.html")


@admin.route("/about",methods=["GET","POST"])
def about():
    return render_template("admin/about.html")