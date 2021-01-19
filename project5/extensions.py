"""Extensions module. Each extension is initialized in the app factory located in app.py."""
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

from project5.utils import jwt_identity, identity_loader


db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()

jwt = JWTManager()
jwt.user_loader_callback_loader(jwt_identity)
jwt.user_identity_loader(identity_loader)
