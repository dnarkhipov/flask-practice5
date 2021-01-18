from project5.database import db, Model, Column


class Customer(Model):
    __tablename__ = 'customers'
    id = Column(db.Integer, primary_key=True)
    mail = Column(db.String(80), unique=True, nullable=False)
    password = Column(db.String(80), nullable=False)
    orders = db.relationship("Order", back_populates="customer")


class Order(Model):
    __tablename__ = 'orders'
    id = Column(db.Integer, primary_key=True)
    customer_id = Column(db.Integer, db.ForeignKey("customers.id"), nullable=False)
    create_dt = Column(db.DateTime, nullable=False)
    customer = db.relationship("Customer", back_populates="orders")
