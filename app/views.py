"""views.py."""
# -*- coding: utf8 -*-

from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('body.html')


@app.route('/about')
def about():
    return render_template('about.html')
