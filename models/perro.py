from db import db
#from sqlalchemy import text

class Perro(db.Model):
    __tablename__ = 'perros'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(150), nullable = False)
    raza = db.Column(db.String(150), nullable = False)
    edad = db.Column(db.Integer, nullable = False)
    peso = db.Column(db.Float, nullable = False)
    id_cuidador = db.Column(db.Integer)
