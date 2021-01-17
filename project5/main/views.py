"""Main site views."""
import json
import random
from flask import Blueprint, render_template, redirect, url_for, session

from .models import Category, Meal


# читаем список продуктов в корзине из session
def read_session_cart() -> list:
    cart = session.get('cart')
    return list() if cart is None or len(cart) == 0 else cart.split(',')


# беседа по поводу включения/исключения static-контента в blueprint
# https://twitter.com/ilCiclotrone/status/1350077793183412228


blueprint = Blueprint('main', __name__, template_folder='templates')


@blueprint.route('/')
def get_main_page():
    categories = Category.query.order_by(Category.title).all()
    menu = {category.title.lower(): random.sample(category.meals, 3) for category in categories}

    # Категория Новинки всегда идет в начале меню, далее сортировка по алфавиту
    promo = menu.pop('новинки', None)
    if promo is not None:
        menu = {'новинки': promo, **menu}

    cart_meals = Meal.query.filter(Meal.id.in_(read_session_cart())).all()

    return render_template(
        'index.html',
        menu=menu,
        cart_meals=cart_meals
    )


@blueprint.route('/addtocart/<meal_id>')
def add_to_cart(meal_id):
    meal = Meal.query.get_or_404(meal_id)

    cart = set(read_session_cart())
    cart.add(meal_id)
    session['cart'] = ','.join(list(cart))

    return redirect(url_for('main.get_cart'))


@blueprint.route('/removefromcart/<meal_id>')
def remove_from_cart(meal_id):
    cart = read_session_cart()
    if len(cart) > 0:
        try:
            cart.remove(meal_id)
            meal = Meal.query.get(meal_id)
            if meal is not None:
                session['last_removed'] = dict(id=meal.id, title=meal.title)
        except ValueError:
            pass
    session['cart'] = ','.join(cart)

    return redirect(url_for('main.get_cart'))


@blueprint.route('/cart')
def get_cart():
    cart_meals = Meal.query.filter(Meal.id.in_(read_session_cart())).all()

    last_removed = session.pop('last_removed', None)

    return render_template(
        'cart.html',
        cart_meals=cart_meals,
        customer=None,
        last_removed=last_removed
    )
