from flask import Blueprint
from flask_restful import Api

main = Blueprint('main', __name__, static_folder='static', template_folder='templates', url_prefix='/main')
main_api = Api(main)

from . import views
