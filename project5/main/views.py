"""Main site views."""
import random
from flask import Blueprint, render_template, redirect, url_for, session

from .models import Category, Meal


blueprint = Blueprint('main', __name__, template_folder='templates')


@blueprint.route('/')
def get_main_page():
    categories = Category.query.order_by(Category.title).all()
    menu = {category.title.lower(): random.sample(category.meals, 3) for category in categories}

    # Категория Новинки всегда идет в начале меню, далее сортировка по алфавиту
    promo = menu.pop('новинки', None)
    if promo is not None:
        menu = {'новинки': promo, **menu}

    return render_template(
        'index.html',
        menu=menu
    )


@blueprint.route('/addtocart/<int:meal_id>')
def get_addtocart(meal_id: int):
    session['cart'] = meal_id
    return redirect(url_for('main.get_cart'))


@blueprint.route('/cart')
def get_cart():
    return render_template(
        'cart.html'
    )
