"""Database module, including the SQLAlchemy database object and DB-related utilities."""
from .extensions import db


Column = db.Column
Model = db.Model
