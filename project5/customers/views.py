from flask import Blueprint, render_template, redirect, url_for, session

# from .models import Category, Meal


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
    return render_template(
        'register.html'
    )


@blueprint.route('/account')
def get_account_page():
    return render_template(
        'account.html'
    )
