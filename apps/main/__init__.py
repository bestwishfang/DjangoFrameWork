from flask import Blueprint
from flask_restful import Api

# static 文件放在Flask() 对象创建目录下，方便部署，每个app 放自己的static 为了解耦，方便移植
# main = Blueprint('main', __name__, static_folder='static', template_folder='templates', url_prefix='/main')

main = Blueprint('main', __name__, template_folder='templates', url_prefix='/main')
main_api = Api(main)

from . import views
