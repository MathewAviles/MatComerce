from flask import render_template, session, request, redirect, url_for, flash
from Tienda import app, db, bcrypt
from .forms import RegistrationForm
from .models import User
from sqlalchemy.exc import IntegrityError
from flask_bcrypt import generate_password_hash
import os

@app.route('/')
def home():
    return render_template('Administrador/index.html', title="Inicio Administrador")




@app.route('/registro', methods=['GET', 'POST'])
def registro():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        try:
            # Generar un hash de la contraseña
            hash_password = generate_password_hash(form.password.data)
            
            user = User(name=form.name.data, username=form.username.data, email=form.email.data,
                        password=hash_password)
            db.session.add(user)
            db.session.commit()  # Guardar cambios en la base de datos
            flash(f'{form.username.data} Gracias por registrarte', 'success')
            return redirect(url_for('home'))
        except IntegrityError:
            # Manejar la excepción de violación de unicidad
            db.session.rollback()  # Revertir los cambios
            flash('El correo electrónico o el nombre de usuario ya están en uso.', 'error')
            return render_template('Administrador/registro.html', title="Registro Administrador", form=form)
    return render_template('Administrador/registro.html', title="Registro Administrador", form=form)


