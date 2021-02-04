# -*- coding: utf-8 -*-

import hashlib
import functools

from flask import request
from flask import session
from flask import render_template, redirect

from . import web, web_api
from .models import WebUser


def set_pwd(password):
    SALT = b'bestwish'
    md5 = hashlib.md5(SALT)
    md5.update(password.encode('utf-8'))
    ret = md5.hexdigest()
    return ret


def login_valid(func):
    @functools.wraps(func)  # 保留原函数的名称
    def inner(*args, **kwargs):
        username = request.cookies.get("web_user")
        id = request.cookies.get("web_id", "0")
        user = WebUser.query.get(int(id))
        session_username = session.get("web_user")
        if user:  # 检测是否有对应id的用户
            if user.username == username and username == session_username:  # 用户名是否对应
                return func(*args, **kwargs)
            else:
                return redirect("/web/login")
        else:
            return redirect("/web/login")

    return inner


@web.route("/register", methods=["GET", "POST"])
def register():
    """
    form表单提交的数据由request.form 接收
    """
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")
        user = WebUser()
        user.username = username
        user.password = set_pwd(password)
        user.email = email
        user.save()
    return render_template("web/register.html")


@web.route("/login", methods=["get", "post"])
def login():
    error = ""
    if request.method == "POST":
        form_data = request.form
        filed = form_data.get('username')
        password = form_data.get("password")
        if filed.endswith('.com'):
            user = WebUser.query.filter_by(email=filed).first()
        else:
            user = WebUser.query.filter_by(username=filed).first()

        if user:
            db_password = user.password
            if set_pwd(password) == db_password:
                response = redirect("/web")
                response.set_cookie("web_user", user.username)
                response.set_cookie("web_email", user.email)
                response.set_cookie("web_id", str(user.id))
                session["web_user"] = user.username
                return response
            else:
                error = "密码错误"
        else:
            error = "用户名不存在"
    else:
        username = request.cookies.get("web_user")
        id = request.cookies.get("id", "0")
        user = WebUser.query.get(int(id))
        session_username = session.get("web_user")
        if user:  # 检测是否有对应id的用户
            if user.username == username and username == session_username:  # 用户名是否对应
                return redirect('/web')

        return render_template("web/login.html", error=error)


@web.route("/logout")
def logout():
    response = redirect("/web/login")
    response.delete_cookie("web_user")
    response.delete_cookie("web_email")
    response.delete_cookie("web_id")
    session.pop("web_user", None)
    # del session["username"]
    return response


@web.route('/')
def index():
    return render_template('web/index.html')
