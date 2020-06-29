from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Nombre de Usuario', validators=[DataRequired(), Length(4,255)])
    password = PasswordField('Contraseña', validators=[DataRequired(), Length(4, 255)])
    remember_me = BooleanField('Mantener mi sesión iniciada')
    submit = SubmitField('Iniciar Sesión')