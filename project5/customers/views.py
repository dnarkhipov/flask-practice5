from flask import Blueprint, render_template, redirect, url_for, request
from sqlalchemy.exc import DBAPIError
from flask_jwt_extended import jwt_required, jwt_optional, create_access_token, current_user

from project5.database import db
from .forms import RegisterForm
from .models import Customer


blueprint = Blueprint('customer', __name__, template_folder='templates')


@blueprint.route('/auth', methods=('get', 'post'))
def auth():
    return render_template(
        'auth.html'
    )


@blueprint.route('/logout')
def logout():
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
            create_access_token(identity=customer, fresh=True)
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
