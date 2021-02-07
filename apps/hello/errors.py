
from flask import render_template

from . import hello


@hello.errorhandler(404)
def page_not_found(e):
    return render_template('hello/errors/404.html'), 404


@hello.errorhandler(500)
def internal_server_error(e):
    return render_template('hello/errors/500.html'), 500

