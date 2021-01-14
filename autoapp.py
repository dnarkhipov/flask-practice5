from flask.helpers import get_debug_flag
from project5.app import create_app
from project5.settings import ProdConfig, DevConfig

config = DevConfig if get_debug_flag() else ProdConfig

app = create_app(config)
