"""Main site views."""
from flask import Blueprint, render_template

from .models import Category, Meal


blueprint = Blueprint('main', __name__, template_folder='templates')


@blueprint.route('/', methods=('get',))
def get_main_page():
    categories = Category.query.all()
    for category in categories:
        meals = category.meals
        pass
    return render_template(
        'index.html'
    )
