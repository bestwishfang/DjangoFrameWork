from flask import Blueprint
from flask_restful import Api

hello = Blueprint('hello', __name__, template_folder='templates', url_prefix='/hello')
hello_api = Api(hello)

from . import views
