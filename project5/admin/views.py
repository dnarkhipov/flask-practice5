from flask_admin.contrib.sqla import ModelView

from project5.customers.models import Customer, Order
from project5.showcase.models import Meal, Category
from project5.extensions import db

customers = ModelView(Customer, db.session)
