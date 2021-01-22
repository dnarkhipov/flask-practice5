from flask import Flask

from project5.extensions import db, migrate, bcrypt, admin, csrf, basic_auth
from project5.settings import ProdConfig
from project5 import showcase, customers

from project5.admin.views import (
    customers as admin_customers, meals as admin_meals,
    categories as admin_categories, orders as admin_orders,
    status as admin_status
)


def create_app(config_object=ProdConfig):
    # An application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/

    app = Flask(__name__.split('.')[0])

    # If a rule ends with a slash but the matched URL does not, redirect to the URL with a trailing slash.
    app.url_map.strict_slashes = False

    app.config.from_object(config_object)

    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    """Register Flask extensions."""
    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)
    bcrypt.init_app(app)
    admin.init_app(app)
    admin.add_views(admin_orders, admin_customers, admin_meals, admin_categories, admin_status)
    basic_auth.init_app(app)


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(showcase.views.blueprint, url_prefix='')
    app.register_blueprint(customers.views.blueprint, url_prefix='')
