from flask import request
from flask import render_template
from . import web, web_api


@web.route('/')
def index():
    return render_template('web_index.html')


@web.route('/login')
def login():
    return 'In web app login'
