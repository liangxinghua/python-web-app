# -*- coding=utf-8 -*-


from flask import render_template, flash, redirect
from forms import LoginForm
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {"nickname": "lxh"}
    posts = [
        {
            "author": {"nickname": "xiaoming"},
            "body": "Beautiful day in Portland!"

        },
        {
            "author": {"nickname": "xiaohua"},
            "body": "Beautiful day in Portland!"

        }
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login required for Name:" + form.name.data)
        flash("Password:" + str(form.pwd.data))
        flash("Remember_me:" + str(form.remeber_me.data))
        return redirect("/")

    return render_template("login.html", title="Sign In", form=form)
