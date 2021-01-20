from project5.extensions import db, bcrypt


class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    mail = db.Column(db.String(80), unique=True, nullable=False)
    # пароль хранится как bcrypt-hash
    password = db.Column(db.Binary(128), nullable=False)

    def __init__(self, mail, password=None, **kwargs):
        """Create instance."""
        db.Model.__init__(self, mail=mail, **kwargs)
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
