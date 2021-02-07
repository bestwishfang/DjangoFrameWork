import wtforms
from flask_wtf import FlaskForm
from wtforms import validators
from wtforms import ValidationError

from .models import User
from settings import EMAIL_PATTERN


def keywords_valid(form, field):
    """
    :param form: 表单
    :param field:  字段
    """
    data = field.data  # 获取input内容（value）
    keywords = ["admin", "GM", "管理员", "版主"]
    if data in keywords:
        raise ValidationError("不可以以敏感词命名")


class FieldValid:
    def __init__(self, message):
        self.message = message

    def __call__(self, form, field):
        data = field.data
        if EMAIL_PATTERN.search(data):
            user = User.query.filter_by(email=data).all()
        else:
            user = User.query.filter_by(username=data).all()
        if not user:
            return None

        raise validators.ValidationError(self.message)


class UserForm(FlaskForm):
    username = wtforms.StringField(label='username',
                                   validators=[
                                       validators.DataRequired(message='用户名不能为空'),
                                       validators.length(min=2, max=8, message="用户名必须大于2位小于8位"),
                                       validators.Regexp(regex=r"[0-9a-zA-Z]{2,8}", message="用户名必须是数字字母下划线"),
                                       FieldValid(message="用户名已存在")
                                   ])
    email = wtforms.StringField(label='email',
                                validators=[
                                    validators.DataRequired(message='邮箱不能为空'),
                                    validators.Regexp(regex=EMAIL_PATTERN, message="邮箱格式错误"),
                                    FieldValid(message="邮箱重复")
                                ])
    password = wtforms.StringField(label="password",
                                   validators=[
                                       validators.length(min=2, max=8, message="密码必须大于2位小于8位")
                                   ])


class RegisterForm(UserForm):
    pass


class LoginForm(UserForm):
    pass


class TaskForm(FlaskForm):
    taskname = wtforms.StringField(label="taskname",
                                   render_kw={
                                       "class": "form-control",
                                       "placeholder": "任务名称"
                                   },
                                   validators=[
                                       validators.DataRequired("用户名不可以为空"),
                                       # validators.length(max=8,min=6), #6-8位
                                       keywords_valid
                                       # validators.Email("必须符合邮箱格式"),
                                   ])
    description = wtforms.StringField(label="description",
                                      render_kw={
                                          "class": "form-control",
                                          "placeholder": "任务描述"
                                      },
                                      validators=[
                                          validators.EqualTo("taskname")  # name和description的内容是否一样
                                      ]
                                      )
    tasktime = wtforms.DateField(label="tasktime",
                                 render_kw={
                                     "class": "form-control",
                                     "placeholder": "任务时间"
                                 })
    public = wtforms.StringField(label="public",
                                 render_kw={
                                     "class": "form-control",
                                     "placeholder": "公布任务人"
                                 })
