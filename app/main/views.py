import os, json
from datetime import datetime
from flask import render_template, session, redirect, url_for, flash, jsonify
from flask_login import login_required
from .forms import CargarArchivoForm
from . import main
from .. import db
from ..models import Usuario, Opinion, Evaluador, Procesamientos, Students
from werkzeug.utils import secure_filename
from ..clases.pazParser import parse

@main.route('/')
@login_required
def index():
    return render_template('menu.html', nombre=session.get('nombre'), current_time=datetime.utcnow())

@main.route('/cargar', methods=['GET', 'POST'])
@login_required
def cargar():
    form = CargarArchivoForm()
    result = None
    if form.validate_on_submit():
        f = form.archivo.data
        filename = secure_filename(f.filename)
        f.save(os.path.join(
            main.root_path, 'files', filename
        ))
        form.archivo.data.save('/cargar' + filename)
        flash('Archivo cargado exitosamente')
        result = parse(os.path.join(
            main.root_path, 'files', filename
        ))
    return render_template('cargar.html', form=form, result=result)

@main.route('/ver')
@login_required
def ver():
    data = Opinion.query.all()
    return render_template('ver.html', data=data)

@main.route('/ver_datos/<tabla>', methods=['GET', 'POST'])
@login_required
def ver_datos(tabla):
    if tabla == 'opiniones':
        data = Opinion.query.all()
    elif tabla == 'evaluador':
        data = Evaluador.query.all()
    elif tabla == 'procesamiento':
        data = Procesamientos.query.all()

    return data