from db import db
#from sqlalchemy import text

class Cuidador(db.Model):
    __tablename__ = 'cuidadores'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(150), nullable = False)
    telefono = db.Column(db.String(150), nullable = False)
