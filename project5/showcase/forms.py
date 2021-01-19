from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import validators
from wtforms.fields.html5 import EmailField, TelField

from project5.utils import phone_validate


class OrderForm(FlaskForm):
    name = StringField('Ваше имя', [validators.InputRequired()])
    address = StringField('Адрес', [validators.InputRequired()])
    mail = EmailField('Электропочта', [validators.InputRequired()])
    phone = TelField('Телефон', [validators.InputRequired(), phone_validate])
