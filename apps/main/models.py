from datetime import datetime
from .. import models


class BaseModel(models.Model):
    __abstract__ = True  # 声明当前类是抽象类，被继承调用不被创建
    id = models.Column(models.Integer, primary_key=True, autoincrement=True)

    def save(self):
        db = models.session()
        db.add(self)
        db.commit()

    def delete(self):
        db = models.session()
        db.delete(self)
        db.commit()


class User(BaseModel):
    __tablename__ = "user"
    username = models.Column(models.String(32))
    password = models.Column(models.String(32))
    email = models.Column(models.String(32))
    c_time = models.Column(models.DateTime, default=datetime.now)

    def __str__(self):
        return self.username
