import os
import re

EMAIL_PATTERN = re.compile(r'^\w+@\w+(\.\w+){0,1}\.(com|cn|net|hk)$')
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
STATICFILES_DIR = os.path.join(BASE_DIR, 'static')


class Config:
    DEBUG = True
    SECRET_KEY = 'personal secret'
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "db.sqlite")  # 数据库地址 sqllite
    # SQLALCHEMY_DATABASE_URI = "mysql://root:123456@192.168.0.103:33306/demo"    # 数据库地址 mysql
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True                                          # 请求结束后自动提交
    SQLALCHEMY_TRACK_MODIFICATIONS = True                                         # flask 1.0 版本之后，添加的选项，目的是跟踪修改


class ProductionConfig(Config):
    DEBUG = False


"""
登录、注册 表单验证
首页

url
methods
endpoint 
    endpoint = options.pop("endpoint", f.__name__)
    self.add_url_rule(rule, endpoint, f, **options)

app.route('/<name>/<int:nid>')
url_for


"""
