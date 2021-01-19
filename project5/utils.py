import phonenumbers
from wtforms import ValidationError

from project5.customers.models import Customer


def phone_validate(form, phone_field):
    try:
        phone = phonenumbers.parse(phone_field.data, region='RU')
        phone_field.data = phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.E164)
    except phonenumbers.NumberParseException:
        raise ValidationError('Введите номер телефона в формате 11 цифр, например +79001234567')


def jwt_identity(customer_id):
    return Customer.query.get(customer_id)


def identity_loader(customer: Customer):
    return customer.id
