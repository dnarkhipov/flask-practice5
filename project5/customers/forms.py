from flask_wtf import FlaskForm
from wtforms import PasswordField
from wtforms import validators
from wtforms.fields.html5 import EmailField


class RegisterForm(FlaskForm):
    mail = EmailField('Электропочта', [validators.InputRequired()])
    password = PasswordField('Пароль', [validators.InputRequired()])
