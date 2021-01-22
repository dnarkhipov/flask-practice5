"""Application configuration."""
from pathlib import Path


class Config(object):
    """Base configuration."""

    SECRET_KEY = 'f33333bd-26e5-40bb-9c5b-9a6cc04454e8'
    APP_DIR = Path(__file__).parent  # This directory
    PROJECT_ROOT = APP_DIR.parent
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ADMIN_SWATCH = 'cosmo'
    BASIC_AUTH_USERNAME = 'admin'
    BASIC_AUTH_PASSWORD = 'admin'


class ProdConfig(Config):
    """Production configuration."""

    ENV = 'prod'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{Config.PROJECT_ROOT}/data/project5.db'


class DevConfig(Config):
    """Development configuration."""

    ENV = 'dev'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{Config.PROJECT_ROOT}/data/project5.db'
    SQLALCHEMY_ECHO = True


class TestConfig(Config):
    """Test configuration."""

    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{Config.PROJECT_ROOT}/data/project5.db'
