from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, current_user
from dotenv import load_dotenv
from db import db, init_db
from models.usuario import Usuario
from models.perro import Perro
from controllers.perro_controller import perro_bp
from controllers.cuidador_controller import cuidador_blueprint
import os
import secrets

load_dotenv()

app = Flask(__name__, template_folder='views')
login_manager = LoginManager(app)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('DB_STRING_CONNECTION')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = secrets.token_urlsafe(16)
app.register_blueprint(perro_bp)
app.register_blueprint(cuidador_blueprint)

db.init_app(app)
# init_db(app)

def cargar():
    usuario1 = Usuario(username = 'martin', password = '123', es_admin=True)
    usuario2 = Usuario(username = 'juan',  password = '456')
    usuario3 = Usuario(username = 'pepe',  password = '789')

    perro1 = Perro(nombre='Rufo', raza='Labrador', edad=7, peso=22.0)
    perro2 = Perro(nombre='Bingo', raza='Pug', edad=2, peso=6.0)
    perro3 = Perro(nombre='Lassie', raza='Collie', edad=3, peso=27.0)
    perro4 = Perro(nombre='Pepe', raza='Pincher', edad=1, peso=2.0)

    db.session.add_all([usuario1, usuario2, usuario3])
    db.session.add_all([perro1, perro2, perro3, perro4])
    db.session.commit()

@login_manager.user_loader
def load_user(id_usuario):
    return Usuario.query.get(id_usuario)

@app.route('/')
def index():
    # cargar()
    return render_template('index.html')
    
@app.route('/login', methods = ["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        usuario = request.form['usuario']
        password = request.form['contrasena']
        print(usuario, password)
        usuario = Usuario.query.filter_by(username=usuario, password=password).first()
        if usuario:
            login_user(usuario)
            return redirect(url_for('perfil'))
        else:
            flash('Usuario y/o contraseña incorrectos')
        print(usuario)
        return render_template('login.html')
    
@app.route('/perfil')
@login_required
def perfil():
    nombre = current_user.username
    return render_template('perfil.html', nombre=nombre)

if __name__ == '__main__':
    app.run(debug=True)