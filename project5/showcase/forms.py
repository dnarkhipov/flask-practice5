import phonenumbers
from flask_wtf import FlaskForm
from wtforms import StringField, validators, ValidationError
from wtforms.fields.html5 import EmailField, TelField


def phone_validate(form, phone_field):
    try:
        phone = phonenumbers.parse(phone_field.data, region='RU')
        phone_field.data = phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.E164)
    except phonenumbers.NumberParseException:
        raise ValidationError('Введите номер телефона в формате 11 цифр, например +79001234567')


class OrderForm(FlaskForm):
    name = StringField('Ваше имя', [validators.InputRequired()])
    address = StringField('Адрес', [validators.InputRequired()])
    mail = EmailField('Электропочта', [validators.InputRequired()])
    phone = TelField('Телефон', [validators.InputRequired(), phone_validate])
