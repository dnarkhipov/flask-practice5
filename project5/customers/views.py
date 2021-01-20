from typing import Optional

from flask import Blueprint, render_template, redirect, url_for, request, session
from sqlalchemy.exc import DBAPIError

from project5.extensions import db
from .forms import AuthForm, RegisterForm
from .models import Customer


def set_current_customer(customer_id):
    session['customer_id'] = customer_id


def unset_current_customer():
    session.pop('customer_id', None)


def get_current_customer() -> Optional[Customer]:
    customer_id = session.get('customer_id', None)
    return Customer.query.get(customer_id) if customer_id else None


blueprint = Blueprint('customers', __name__, template_folder='templates')


@blueprint.route('/auth', methods=('get', 'post'))
def auth():
    form = AuthForm()

    if request.method == 'POST':
        if form.validate():
            customer = Customer.query.filter_by(mail=form.mail.data).first()
            if customer is not None and customer.check_password(form.password.data):
                set_current_customer(customer.id)
                return redirect(url_for('showcase.get_account_page'))
            else:
                pass

    return render_template(
        'auth.html',
        form=form
    )


@blueprint.route('/logout')
def logout():
    unset_current_customer()
    return redirect(url_for('showcase.get_main_page'))


@blueprint.route('/register', methods=('get', 'post'))
def register():
    form = RegisterForm()

    if request.method == 'POST':
        if form.validate():
            customer = Customer(mail=form.mail.data, password=form.password.data)
            db.session.add(customer)
            try:
                db.session.commit()
            except DBAPIError as err:
                return f'Internal DBAPI error: {err}', 500
            set_current_customer(customer.id)
            return redirect(url_for('showcase.get_account_page'))

    return render_template(
        'register.html',
        form=form
    )
