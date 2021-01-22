from flask import redirect, Response
from flask_admin.contrib.sqla import ModelView
from werkzeug.exceptions import HTTPException

from project5.customers.models import Customer
from project5.showcase.models import Meal, Category, Order, OrderStatus
from project5.extensions import db, basic_auth


class AuthException(HTTPException):
    def __init__(self, message):
        super().__init__(
            message,
            Response(
                "You could not be authenticated. Please refresh the page.",
                401,
                {'WWW-Authenticate': 'Basic realm="Login Required"'}
            )
        )


class AdminView(ModelView):
    def is_accessible(self):
        if not basic_auth.authenticate():
            raise AuthException('Not authenticated.')
        else:
            return True

    def inaccessible_callback(self, name, **kwargs):
        return redirect(basic_auth.challenge())


class CustomersView(AdminView):
    can_create = False
    column_exclude_list = ['password', ]


customers = CustomersView(model=Customer, session=db.session, name='Клиенты')
categories = AdminView(model=Category, session=db.session, name='Категории')
meals = AdminView(model=Meal, session=db.session, name='Блюда')
status = AdminView(model=OrderStatus, session=db.session, name='Статусы')
orders = AdminView(model=Order, session=db.session, name='Заказы')
