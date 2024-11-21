from models.cuidador import Cuidador
from models.perro import Perro
from flask import Blueprint, render_template
import sqlalchemy as sql
from db import db

cuidador_blueprint = Blueprint('cuidador_bp', __name__, url_prefix="/cuidadores")

@cuidador_blueprint.route('/')
def index():
    #cuidadores = Cuidador.query.all()
    resultado = db.session.query(Perro, Cuidador).join(Cuidador, Perro.id_cuidador == Cuidador.id).all()

    print(resultado)

    for perros, cuidadores in resultado:
        print(perros.nombre, cuidadores.nombre)

    return render_template('cuidadores.html', cuidadores = resultado)

@cuidador_blueprint.route('/mario')
def asigna():
    mario = Cuidador.query.filter_by(nombre = 'Mario').first().id

    #mario = Perro.query.filter(Perro.peso < 7).all()
    db.session().query(Perro).filter(Perro.peso < 7).update({"id_cuidador": mario})
    db.session.commit()
    perros_de_mario = Perro.query.filter_by(id_cuidador = mario).all()

    return render_template('mario.html', resultado = perros_de_mario)
