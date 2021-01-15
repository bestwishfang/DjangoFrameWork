import pymysql

from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy

pymysql.install_as_MySQLdb()

csrf = CSRFProtect()
models = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object('settings.Config')
    # models.init_app(app)  # models = SQLAlchemy(app) 加载数据库
    # csrf.init_app(app)
    from .main import main
    from .web import web
    app.register_blueprint(main)
    app.register_blueprint(web)
    return app
