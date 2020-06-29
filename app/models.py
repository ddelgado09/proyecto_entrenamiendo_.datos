from . import db
from . import login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(id_usuario):
    return Usuario.query.get(int(id_usuario))

class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuario'
    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(255))
    password_usuario = db.Column(db.String(255))

    def __repr__(self):
        return '<Usuario %r>' % self.nombre_usuario

    def get_id(self):
        return self.id_usuario

class Evaluador(db.Model):
    __tablename__ = 'evaluador'
    idevaluador = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))
    idopinion = db.Column(db.Integer, db.ForeignKey('opinion.idopinion'))
    clasifiopi = db.Column(db.String(255))
    clasifiopi1 = db.Column(db.String(255))
    idevaluacion = db.Column(db.Integer, primary_key=True, nullable=False)

    def __repr__(self):
        return '<Evaluador %r %r $r>' % (self.idevaluador, self.clasifiopi, self.clasifiopi1)

class Opinion(db.Model):
    __tablename__ = 'opinion'
    timestamp = db.Column(db.String(255), primary_key=True, nullable=False)
    student = db.Column(db.String(255), nullable=False, primary_key=True)
    opinion = db.Column(db.String, nullable=False)
    idopinion = db.Column(db.Integer, nullable=False)
    edad = db.Column(db.Integer)
    semester = db.Column(db.String(255))
    nombres = db.Column(db.String(255))
    procesamiento = db.relationship('Procesamientos', backref='opinion')

    def __repr__(self):
        return '<Opinion %r %r %r %r %r>' % (self.student, self.opinion, self.edad, self.semester, self.nombres)
    
class Procesamientos(db.Model):
    __tablename__ = 'procesamientos'
    id_procesamiento = db.Column(db.Integer, primary_key=True, nullable=False)
    plagio = db.Column(db.String)
    largo = db.Column(db.String)
    idopinion = db.Column(db.Integer, db.ForeignKey('opinion.idopinion'))
    url = db.Column(db.String)

    def __repr__(self):
        return '<Procesamientos %r %r %r>' % self.plagio % self.largo % self.url

class Students(db.Model):
    __tablename__ = 'students'
    semestre = db.Column(db.Text)
    programa = db.Column(db.Text)
    tdocumento = db.Column(db.Text)
    numero = db.Column(db.Text)
    codigo = db.Column(db.Text)
    codigoinscrip = db.Column(db.Text)
    nombreestudiante = db.Column(db.Text, nullable=False, primary_key=True)
    genero = db.Column(db.Text)
    colegio = db.Column(db.Text)
    tipocolegio = db.Column(db.Text)
    ciudadcolegio = db.Column(db.Text)
    estado = db.Column(db.Text)
    especialidad = db.Column(db.Text)
    estadocivil = db.Column(db.Text)
    tarjetamilitar = db.Column(db.Text)
    paisnacimiento = db.Column(db.Text)
    deptonacimiento = db.Column(db.Text)
    ciudadnacimiento = db.Column(db.Text)
    fechanacimiento = db.Column(db.Text)
    paisrecidencia = db.Column(db.Text)
    deptorecidencia = db.Column(db.Text)
    ciudadresidencia = db.Column(db.Text)
    numhijos = db.Column(db.Text)
    tipovovienda = db.Column(db.Text)
    numpersonasacargo = db.Column(db.Text)
    estrato = db.Column(db.Text)
    sisben = db.Column(db.Text)
    deusacasa = db.Column(db.Text)
    actividadeconomica = db.Column(db.Text)
    rangosalarial = db.Column(db.Text)
    financiamatricula = db.Column(db.Text)
    grupodiscapacidad = db.Column(db.Text)
    discapacidad = db.Column(db.Text)
    resguardoindigena = db.Column(db.Text)
    grupoetnico = db.Column(db.Text)
    victima = db.Column(db.Text)
    desplazado = db.Column(db.Text)
    students = db.Column(db.String(255))
    temporal = db.Column(db.String)
    idstudent = db.Column(db.Integer, nullable=False)
