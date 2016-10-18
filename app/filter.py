# -*- coding:utf-8 -*-
from datetime import datetime
from app import app


@app.template_filter("datetime_format")
def datetime_filter(s):
    return s.strftime("%Y-%m-%d %H:%M:%S")


@app.template_filter("reverse")
def reverse(list):
    return list[::-1]