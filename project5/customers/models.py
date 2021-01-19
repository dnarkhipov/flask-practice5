from datetime import datetime
from project5.database import db, Model, Column
from project5.extensions import bcrypt


class Customer(Model):
    __tablename__ = 'customers'
    id = Column(db.Integer, primary_key=True)
    mail = Column(db.String(80), unique=True, nullable=False)
    # пароль хранится как bcrypt-hash
    password = Column(db.Binary(128), nullable=False)
    orders = db.relationship("Order", back_populates="customer")

    def __init__(self, mail, password=None, **kwargs):
        """Create instance."""
        Model.__init__(self, mail=mail, **kwargs)
        if password:
            self.set_password(password)
        else:
            self.password = None

    def set_password(self, password):
        """Set password."""
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, value):
        """Check password."""
        return bcrypt.check_password_hash(self.password, value)

    def __repr__(self):
        """Represent instance as a unique string."""
        return f'<Customer({self.mail})>'


class Order(Model):
    __tablename__ = 'orders'
    id = Column(db.Integer, primary_key=True)
    customer_id = Column(db.Integer, db.ForeignKey("customers.id"), nullable=False)
    create_dt = Column(db.DateTime, nullable=False, default=datetime.now())
    customer = db.relationship("Customer", back_populates="orders")
