from flask_admin.contrib.sqla import ModelView

from project5.customers.models import Customer
from project5.showcase.models import Meal, Category, Order
from project5.extensions import db


customers = ModelView(Customer, db.session)
categories = ModelView(Category, db.session)
meals = ModelView(Meal, db.session)
orders = ModelView(Order, db.session)
