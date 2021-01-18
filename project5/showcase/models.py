from project5.database import db, Model, Column


class Category(Model):
    __tablename__ = 'categories'
    id = Column(db.Integer, primary_key=True)
    title = Column(db.String(80), nullable=False, unique=True)
    meals = db.relationship('Meal', uselist=True, back_populates="category")


class Meal(Model):
    __tablename__ = 'meals'
    id = Column(db.Integer, primary_key=True)
    category_id = Column(db.Integer, db.ForeignKey("categories.id"), nullable=False)
    title = Column(db.String(80), nullable=False)
    price = Column(db.Integer, nullable=False)
    description = Column(db.String(250), nullable=False)
    picture = Column(db.String(80), nullable=False)
    category = db.relationship("Category", back_populates="meals")
