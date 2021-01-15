from flask import request
from flask import render_template
from . import main, main_api


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/login')
def login():
    return 'In main app login'
