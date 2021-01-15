"""Main site views."""
import random
from flask import Blueprint, render_template

from .models import Category, Meal


blueprint = Blueprint('main', __name__, template_folder='templates')


@blueprint.route('/', methods=('get',))
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
