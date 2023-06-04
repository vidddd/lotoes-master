"""Flask application creation factory."""
import sys, os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config.config import config
from .mount_blueprints import mount_blueprints
from flask_migrate import Migrate
from flask_mail import Mail
from .extensions import register_error_handlers, configure_logging2

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'usuarios.login'

def setdefaultencoding():
    if sys.version[0] == '2':
        reload(sys)
        sys.setdefaultencoding('utf-8')

def create_app(set_utf=True):
    """App creation factory based on the FLASK_CONFIG env var."""
    if set_utf:
        setdefaultencoding()
    
    config_name = os.getenv('FLASK_CONFIG') or 'default'

    app = Flask(__name__, instance_relative_config=True) 
    app.config.from_object(config[config_name])
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    login_manager.init_app(app)

    mount_blueprints(app, config_name)
    register_error_handlers(app)
    configure_logging2(app)

    return app
