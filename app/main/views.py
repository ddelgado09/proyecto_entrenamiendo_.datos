import os, json
from datetime import datetime
from flask import render_template, session, redirect, url_for, flash, jsonify, request
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
    data = None
    if not request.script_root:
        request.script_root = url_for('main.index', _external=True)

    opiniones = Opinion.query.order_by(Opinion.idopinion.asc()).all()
    estudiantes = Students.query.order_by(Students.numero.asc()).all()
    procesamientos = Procesamientos.query.order_by(Procesamientos.id_procesamiento.asc()).all()
    evaluador = Evaluador.query.order_by(Evaluador.idevaluador.asc()).all()

    return render_template('ver.html', 
        opiniones=opiniones, 
        estudiantes=estudiantes, 
        procesamientos=procesamientos, 
        evaluador=evaluador
        )

@main.route('/ver_datos/<tabla>')
@login_required
def ver_datos(tabla):
    pass