"""Extensions module. Each extension is initialized in the app factory located in app.py."""
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_admin import Admin, AdminIndexView
from flask_wtf.csrf import CSRFProtect
from flask_basicauth import BasicAuth

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
csrf = CSRFProtect()
basic_auth = BasicAuth()


# скрываем вкладку Home в интерфейсе администратора
# https://stackoverflow.com/questions/61624338/flask-admin-remove-home-button
class DashboardView(AdminIndexView):
    def is_visible(self):
        # This view won't appear in the menu structure
        return False


admin = Admin(name='Администратор', index_view=DashboardView())
