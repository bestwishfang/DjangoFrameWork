# -*- coding: utf-8 -*-

from flask import flash, render_template, redirect, url_for

from . import hello, hello_api
from .forms import HelloForm
from .models import HelloMessage


@hello.route('/', methods=['GET', 'POST'])
def index():
    form = HelloForm()
    if form.validate_on_submit():
        msg_name = form.msg_name.data
        body = form.body.data

        message = HelloMessage(msg_name=msg_name, body=body)
        message.save()
        flash('Your message have been sent to the hello web.')
        return redirect(url_for('hello.index'))

    messages = HelloMessage.query.order_by(HelloMessage.c_time.desc()).all()
    return render_template('hello/index.html', form=form, messages=messages)
