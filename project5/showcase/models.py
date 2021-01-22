from datetime import datetime
from project5.extensions import db


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False, unique=True)
    meals = db.relationship('Meal', uselist=True, back_populates="category")

    def __str__(self):
        return f'{self.title}'


class Meal(db.Model):
    __tablename__ = 'meals'
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=False)
    title = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    picture = db.Column(db.String(80), nullable=False)
    category = db.relationship("Category", back_populates="meals")

    def __str__(self):
        return f'{self.title}'


order_meals = db.Table(
    'order_meals',
    db.Column('order_id', db.Integer, db.ForeignKey('orders.id'), nullable=False),
    db.Column('meal_id', db.Integer, db.ForeignKey('meals.id'), nullable=False)
)


class OrderStatus(db.Model):
    __tablename__ = 'order_status'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __str__(self):
        return f'{self.name}'


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    status_id = db.Column(db.Integer, db.ForeignKey('order_status.id'), nullable=False, default=0)
    status = db.relationship('OrderStatus')
    create_dt = db.Column(db.DateTime, nullable=False, default=datetime.now())
    total = db.Column(db.Integer, nullable=False, default=0)
    mail = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    address = db.Column(db.String(80), nullable=False)
    meals = db.relationship('Meal', secondary=order_meals)
