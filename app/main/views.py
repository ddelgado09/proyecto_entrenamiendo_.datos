from datetime import datetime
from flask import render_template, session, redirect, url_for, flash
from . import main
from .forms.LoginForm import LoginForm
from .. import db
from ..models import Usuario

@main.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        user_db = Usuario.query.filter_by(nombre_usuario=form.username.data).first()
        if user_db is not None and user_db.password_usuario == form.password.data:
            session['nombre'] = form.username.data
            return redirect(url_for('.menu'))
        else:
            flash('Usuario o contraseña incorrectos')

    return render_template('login.html', form=form, current_time=datetime.utcnow())

@main.route('/menu')
def menu():
    return render_template('menu.html', nombre=session.get('nombre'), current_time=datetime.utcnow())