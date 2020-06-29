from flask import render_template, redirect, request, url_for, flash, session
from flask_login import login_user, logout_user, login_required
from .forms import LoginForm
from . import auth
from ..models import Usuario

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Usuario.query.filter_by(nombre_usuario=form.username.data).first()
        if user is not None and user.password_usuario == form.password.data:
            login_user(user, form.remember_me.data)

            next = request.args.get('next')
            session['nombre'] = form.username.data
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)
        flash('Usuario o contraseña incorrectos')
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado la sesión')
    return redirect(url_for('main.index'))