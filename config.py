# config.py
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-me')

    # MySQL database URI
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URI',
        'mysql+pymysql://root:root123@127.0.0.1/flask_auth_db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-Session config
    SESSION_TYPE = 'sqlalchemy'               # store sessions in DB
    SESSION_SQLALCHEMY_TABLE = 'sessions'     # table name for sessions
    PERMANENT_SESSION_LIFETIME = 60 * 60 * 24 * 7  # 7 days
