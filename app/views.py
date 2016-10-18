# -*- coding:utf-8 -*-

import datetime

from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import current_user, login_user, logout_user, login_required

from forms import LoginForm, SignUpForm, PostForm
from app import app, lm, db
from app.models import User, Post


@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
@app.route('/index')
def index():
    user = current_user
    posts = Post.query.all()
    return render_template("index.html", title="Home", user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/')

    form = LoginForm()
    if form.validate_on_submit():
        user = User.login_check(request.form.get('user_name'))
        if user:
            login_user(user)
            user.last_seen = datetime.datetime.now()
            flash('Your name: ' + request.form.get('user_name'))
            flash('remember me? ' + str(bool(request.form.get('remeber_me'))))
            return redirect(url_for("index", useri_id=current_user.id))
        else:
            flash('Login failed, Your name is not exist!')
            return redirect('/login')

    return render_template("login.html", title="Sign In", form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route('/sign-up', methods=["GET", "POST"])
def sign_up():
    form = SignUpForm()
    user = User()
    if form.validate_on_submit():
        user_name = request.form.get("user_name")
        user_email = request.form.get("user_email")
        if not len(user_name) and not len(user_email):
            flash("error: The user's name or email is invalid!")

        register_check = User.query.filter(db.and_(User.nickname == user_name,
                                                   User.email == user_email)
                                           ).first()
        if register_check:
            flash("error: The user's name or email already exists!")
            return redirect('/sign-up')

        try:
            user.nickname = user_name
            user.email = user_email
            db.session.add(user)
            db.session.commit()
            login_user(user)
            user.last_seen = datetime.datetime.now()
        except:
            flash("The Database error!")
            return redirect('/sign-up')

        flash("Sign up successful!")
        return redirect('/index')
    return render_template("sign-up.html", title="sign up", form=form)


@app.route('/publish', methods=["GET", "POST"])
@login_required
def publish():
    form = PostForm()
    post = Post()
    if form.validate_on_submit():
        post.title = request.form.get('title')
        post.body = request.form.get('body')
        post.timestamp = datetime.datetime.now()
        post.user_id = current_user.id
        try:
            db.session.add(post)
            db.session.commit()
        except:
            flash("database error!")
            return url_for('publish')
        flash("publish successful!")
        return redirect(url_for('index'))

    return render_template('publish.html', form=form)
