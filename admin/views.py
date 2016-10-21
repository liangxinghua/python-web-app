# -*- coding:utf-8 -*-
import json
from flask import render_template, make_response, request

from admin import admin
from admin.upload.config import config
from admin.upload.FileUpload import  FileUpload


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


@admin.route("/filehandler",methods=["GET","POST"])
def filehandler():
    action = request.args.get("action")
    if action == "uploadimage":
        if request.method=="POST":
            file = request.files[config["imageFieldName"]]
            print file
            ul = FileUpload(file)
            return json.dumps(ul.save_file())
    elif action == "uploadfile":
        pass
    elif action=="config":
        return json.dumps(config)
    return "ok"
