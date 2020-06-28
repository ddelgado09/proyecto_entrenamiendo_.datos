from . import db

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(255))
    password_usuario = db.Column(db.String(255))

    def __repr__(self):
        return '<Usuario %r>' % self.nombre_usuario