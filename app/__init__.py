# app/__init__.py
from flask import Flask
from .extensions import db, login_manager
from .auth import auth_bp
from .views import main_bp
from config import Config
from flask_session import Session


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # -------------------------------
    # Configure Flask-Session to use your existing SQLAlchemy instance
    # -------------------------------
    # tell Flask-Session to use existing db
    app.config['SESSION_SQLALCHEMY'] = db
    sess = Session(app)  # initialize session AFTER config

    with app.app_context():
        # Register blueprints
        app.register_blueprint(auth_bp)
        app.register_blueprint(main_bp)

        # Create all tables, including session table
        db.create_all()

    # Flask-Login settings
    login_manager.login_view = 'auth.signin'
    login_manager.login_message_category = 'warning'

    return app
