from flask import render_template, session, request, redirect, url_for
from Tienda import app, db


@app.route('/')
def home():
    return "Pagina de inicio de mi aplicación web"

@app.route('registro')
def registro():
    return render_template('Administrador/registro.html',title="Registro Administrador")