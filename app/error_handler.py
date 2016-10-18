# -*- conding:utf-8 -*-

from flask import render_template, make_response
from app import app


@app.errorhandler(404)
def page_not_found(error):
    resp = make_response(render_template("page_not_found.html"), 404)
    resp.headers["X-somthing"] = error
    return resp


@app.errorhandler(500)
def inner_error(error):
    return render_template("inner_error.html"), 500
