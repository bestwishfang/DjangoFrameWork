import pymysql

from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

from settings import STATICFILES_DIR

pymysql.install_as_MySQLdb()

csrf = CSRFProtect()
models = SQLAlchemy()
# bootstrap = Bootstrap()


def create_app():
    app = Flask(__name__, static_folder=STATICFILES_DIR)
    app.config.from_object('settings.Config')
    models.init_app(app)  # models = SQLAlchemy(app) 加载数据库
    csrf.init_app(app)    # csrf = CSRFProtect(app)  Enable CSRF protection globally for a Flask app.
    # bootstrap.init_app(app)

    from .main import main
    from .web import web
    from .hello import hello
    app.register_blueprint(main)
    app.register_blueprint(web)
    app.register_blueprint(hello)

    return app
