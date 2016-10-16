# -*- coding:utf-8 -*-

from flask_wtf import Form
from wtforms import TextField, BooleanField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import required, email, length


class LoginForm(Form):
    user_name = TextField("user name", validators=[required(), length(max=15)])
    remeber_me = BooleanField("remember me", default=False)
    submit = SubmitField("Log In")


class SignUpForm(Form):
    user_name = TextField("user name", validators=[required(), length(max=15)])
    user_email = TextField("email", validators=[required(), length(max=128), email()])
    remeber_me = BooleanField("remember me", default=False)
    submit = SubmitField("Sign Up")


class PostForm(Form):
    title = TextField("title", validators=[required(), length(max=100)])
    body = TextAreaField("content", validators=[required(), length(max=5000)])
