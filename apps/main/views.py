# -*- coding: utf-8 -*-

import hashlib
import functools

from flask import request
from flask import session
from flask import render_template, redirect

from . import main, main_api
from .models import User
from .forms import RegisterForm, LoginForm
from settings import EMAIL_PATTERN


def set_pwd(password):
    SALT = b'bestwish'
    md5 = hashlib.md5(SALT)
    md5.update(password.encode('utf-8'))
    ret = md5.hexdigest()
    return ret


def login_valid(func):
    @functools.wraps(func)  # 保留原函数的名称 endpoint
    def inner(*args, **kwargs):
        username = request.cookies.get("username")
        id = request.cookies.get("id", "0")
        user = User.query.get(int(id))
        session_username = session.get("username")
        if user:  # 检测是否有对应id的用户
            if user.username == username and username == session_username:  # 用户名是否对应
                return func(*args, **kwargs)
            else:
                return redirect("/login")
        else:
            return redirect("/login")

    return inner


@main.route("/register", methods=["GET", "POST"])
def register():
    """
    form表单提交的数据由request.form 接收
    """
    form = RegisterForm()
    if request.method == "POST":
        data = request.form
        print(f'data: \n{data}')
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")
        user = User()
        user.username = username
        user.password = set_pwd(password)
        user.email = email
        user.save()
        return redirect('/login')

    return render_template("main/register.html", form=form)


@main.route("/login", methods=['GET', 'POST'])
def login():
    error = ""
    form = LoginForm()
    if request.method == "POST":
        form_data = request.form
        filed = form_data.get('username')
        password = form_data.get("password")
        if EMAIL_PATTERN.search(filed):
            user = User.query.filter_by(email=filed).first()
        else:
            user = User.query.filter_by(username=filed).first()

        if user:
            db_password = user.password
            if set_pwd(password) == db_password:
                response = redirect('/')
                response.set_cookie("username", user.username)
                response.set_cookie("email", user.email)
                response.set_cookie("id", str(user.id))
                session["username"] = user.username
                return response
            else:
                error = "密码错误"
        else:
            error = "用户名不存在"
    else:
        username = request.cookies.get("username")
        id = request.cookies.get("id", "0")
        user = User.query.get(int(id))
        session_username = session.get("username")
        if user:  # 检测是否有对应id的用户
            if user.username == username and username == session_username:  # 用户名是否对应
                return redirect('/')

    return render_template("main/login.html", error=error, form=form)


@main.route("/logout")
def logout():
    response = redirect("/login")
    response.delete_cookie("username")
    response.delete_cookie("email")
    response.delete_cookie("id")
    session.pop("username", None)
    # del session["username"]
    return response


@main.route('/')
def index():
    return render_template('main/index.html')

