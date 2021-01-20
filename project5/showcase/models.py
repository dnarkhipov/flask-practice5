from datetime import datetime
from project5.extensions import db


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False, unique=True)
    meals = db.relationship('Meal', uselist=True, back_populates="category")


class Meal(db.Model):
    __tablename__ = 'meals'
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=False)
    title = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    picture = db.Column(db.String(80), nullable=False)
    category = db.relationship("Category", back_populates="meals")


order_meals = db.Table(
    'order_meals',
    db.Column('order_id', db.Integer, db.ForeignKey('meals.id'), nullable=False),
    db.Column('meal_id', db.Integer, db.ForeignKey('orders.id'), nullable=False)
)


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    create_dt = db.Column(db.DateTime, nullable=False, default=datetime.now())
    total = db.Column(db.Integer, nullable=False, default=0)
    status = db.Column(db.Integer, nullable=False, default=0)
    mail = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    address = db.Column(db.String(80), nullable=False)
    meals = db.relationship('Meal', secondary=order_meals)
