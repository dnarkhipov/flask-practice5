from flask_wtf import FlaskForm
from wtforms import PasswordField, validators, ValidationError
from wtforms.fields.html5 import EmailField


from project5.customers.models import Customer


def mail_validate(form, mail_field):
    customer = Customer.query.filter_by(mail=mail_field.data).first()
    if customer:
        raise ValidationError('Клиент с таким адресом уже зарегистрирован')


class AuthForm(FlaskForm):
    mail = EmailField('Электропочта', [validators.InputRequired()])
    password = PasswordField('Пароль', [validators.InputRequired()])


class RegisterForm(FlaskForm):
    mail = EmailField('Электропочта', [
        validators.InputRequired(),
        validators.Email(message='Введите правильный адрес'),
        mail_validate])
    password = PasswordField('Пароль', [
        validators.InputRequired(),
        validators.Length(min=5, max=-1, message='Длина пароля не менее 5 символов')
    ])
