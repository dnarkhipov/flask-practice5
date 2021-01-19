from flask import Flask, render_template, send_from_directory, redirect, url_for, request
from flask_wtf.csrf import CSRFProtect
from project5.extensions import db, migrate, bcrypt, jwt

from project5.settings import ProdConfig
from project5 import showcase, customers


csrf = CSRFProtect()


def create_app(config_object=ProdConfig):
    """An application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
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
    jwt.init_app(app)


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(showcase.views.blueprint, url_prefix='')
    app.register_blueprint(customers.views.blueprint, url_prefix='')
