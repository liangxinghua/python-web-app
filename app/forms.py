# -*- coding=utf-8 -*-


from flask_wtf import Form
from wtforms import TextField, BooleanField, PasswordField
from wtforms.validators import required


class LoginForm(Form):
    name = TextField("Name", validators=[required()])
    pwd = PasswordField("Pwd", validators=[required()])
    remeber_me = BooleanField("Remeber_me",default=False)

