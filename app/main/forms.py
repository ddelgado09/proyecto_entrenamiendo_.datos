from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_wtf.file import FileField, FileRequired, FileAllowed

class CargarArchivoForm(FlaskForm):
    archivo = FileField('Cargar el archivo..', validators=[
        FileRequired(), 
        FileAllowed(['doc', 'docx'], 'Formato no válido')
        ])
    submit = SubmitField('Cargar')
