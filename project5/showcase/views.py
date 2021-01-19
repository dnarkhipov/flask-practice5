"""Main site views."""
import json
import random
from flask import Blueprint, render_template, redirect, url_for, session

from project5.customers import get_current_customer
from .models import Category, Meal
from .forms import OrderForm


# читаем список продуктов в корзине из session
def read_session_cart() -> list:
    cart = session.get('cart')
    return list() if cart is None or len(cart) == 0 else cart.split(',')

# беседа по поводу включения/исключения static-контента в blueprint
# https://twitter.com/ilCiclotrone/status/1350077793183412228


blueprint = Blueprint('showcase', __name__, template_folder='templates')


@blueprint.app_template_filter('count_formatter')
def count_formatter(count: int):
    # примитивное склонение слова 'блюдо' в зависимости от количества
    if count in [1, 21, 31]:
        s_patch = 'блюдо'
    elif count in [2, 3, 4, 22, 23, 24]:
        s_patch = 'блюда'
    else:
        s_patch = 'блюд'

    return f'{count} {s_patch}'


@blueprint.route('/')
def get_main_page():
    categories = Category.query.order_by(Category.title).all()
    menu = {category.title.lower(): random.sample(category.meals, 3) for category in categories}

    # Категория Новинки всегда идет в начале меню, далее сортировка по алфавиту
    promo = menu.pop('новинки', None)
    if promo is not None:
        menu = {'новинки': promo, **menu}

    cart_meals = Meal.query.filter(Meal.id.in_(read_session_cart())).all()
    customer = get_current_customer()

    return render_template(
        'index.html',
        menu=menu,
        cart_meals=cart_meals,
        customer=customer
    )


@blueprint.route('/addtocart/<meal_id>')
def add_to_cart(meal_id):
    meal = Meal.query.get_or_404(meal_id)

    cart = set(read_session_cart())
    cart.add(meal_id)
    session['cart'] = ','.join(list(cart))

    return redirect(url_for('showcase.get_cart'))


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

    return redirect(url_for('showcase.get_cart'))


@blueprint.route('/cart', methods=('get', 'post'))
def get_cart():
    form = OrderForm()

    cart_meals = Meal.query.filter(Meal.id.in_(read_session_cart())).all()
    last_removed = session.pop('last_removed', None)
    customer = get_current_customer()

    return render_template(
        'cart.html',
        cart_meals=cart_meals,
        customer=customer,
        last_removed=last_removed
    )
