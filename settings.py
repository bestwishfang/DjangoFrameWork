import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# STATICFILES_DIR = os.path.join(BASE_DIR, 'static')  # 配置该参数 感觉没啥用


class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "db.sqlite")  # 数据库地址 sqllite
    # SQLALCHEMY_DATABASE_URI = "mysql://root:123456@192.168.0.103:33306/demo"  # 数据库地址 mysql
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True  # 请求结束后自动提交
    SQLALCHEMY_TRACK_MODIFICATIONS = True  # flask1版本之后，添加的选项，目的是跟踪修改


class RunConfig(Config):
    DEBUG = False


"""
登录、注册 表单验证
首页



"""