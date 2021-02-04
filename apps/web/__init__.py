from flask import Blueprint
from flask_restful import Api

web = Blueprint('web', __name__, template_folder='templates', url_prefix='/web')
web_api = Api(web)

from . import views
