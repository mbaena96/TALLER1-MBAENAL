from models.perro import Perro
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user

perro_bp = Blueprint('perro_bp', __name__, url_prefix="/perros")

@perro_bp.route('/')
@login_required
def ver_perros():
    if current_user.es_admin:
        perros = Perro.query.all()
        return render_template('perros.html', perros = perros)
    else:
        flash('Necesita permisos de administrador para ver la lista de perros')
        return redirect(url_for('perfil'))

@perro_bp.route('/lassie')
@login_required
def index_2():
    if current_user.es_admin:      
        perros = Perro.query.filter_by(nombre='Lassie').all()
        return render_template('perros.html', perros = perros, texto = "Lista de perros llamados Lassie")
    else:
        flash('Necesita permisos de administrador para ver la lista de perros')
        return redirect(url_for('perfil'))