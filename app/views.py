"""views.py."""
# -*- coding: utf8 -*-

from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('body.html')


@app.route('/about')
@app.route('/sobremi')
def sobremi():
    return render_template('about.html')


@app.route('/clasesdeguitarra')
def guitarraelectrica():
    return render_template('clasesdeguitarra.html')


@app.route('/guitarraclasicaocriolla')
def guitarraclasicaocriolla():
    return render_template('guitarraclasicaocriolla.html')


@app.route('/guitarraacustica')
def guitarraacustica():
    return render_template('guitarraacustica.html')


@app.route('/contacto')
def contacto():
    return render_template('contacto.html')


@app.route('/cursodeguitarra')
def cursodeguitarra():
    return render_template('cursodeguitarra.html')


@app.route('/login')
def login():
    return render_template('login')


@app.route('/formacionmusical')
def formacion():
    return render_template('formacion')

