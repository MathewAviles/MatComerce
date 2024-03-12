from flask import render_template, session, request, redirect, url_for, flash
from Tienda import app, db
from .forms import RegistrationForm


@app.route('/')
def home():
    return "Página de inicio de mi aplicación2"


@app.route('/registro', methods=['GET', 'POST'])
def registro():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        #user = User(form.username.data, form.email.data,
                  #  form.password.data)
        #db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('Administrador/registro.html', title="Registro Administrador", form=form)

