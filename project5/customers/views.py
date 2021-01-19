from flask import Blueprint, render_template, redirect, url_for, request, session
from sqlalchemy.exc import DBAPIError

from project5.extensions import db
from .forms import AuthForm, RegisterForm
from .models import Customer


def get_current_customer():
    customer_id = session.get('customer_id', None)
    if customer_id:
        customer = Customer.query.get(customer_id)
    else:
        customer = None
    return customer


blueprint = Blueprint('customers', __name__, template_folder='templates')


@blueprint.route('/auth', methods=('get', 'post'))
def auth():
    form = AuthForm()

    if request.method == 'POST':
        if form.validate():
            customer = Customer.query.filter_by(mail=form.mail.data).first()
            if customer is not None and customer.check_password(form.password.data):
                session['customer_id'] = customer.id
                return redirect(url_for('showcase.get_main_page'))
            else:
                pass

    return render_template(
        'auth.html',
        form=form
    )


@blueprint.route('/logout')
def logout():
    session.pop('customer_id', None)
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
            session['customer_id'] = customer.id
            return redirect(url_for('showcase.get_main_page'))

    return render_template(
        'register.html',
        form=form
    )


@blueprint.route('/account')
def get_account_page():
    return render_template(
        'account.html'
    )
