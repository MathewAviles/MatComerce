from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
import os

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///matcomerce.db"
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URL")
#postgres://dbmatcomerce_user:VlSbUtyyJNJ7NhM097eDZWC0XVhc6y6A@dpg-cnoh6cg21fec73dvdu00-a.oregon-postgres.render.com/dbmatcomerce
# initialize the app with the extension
db = SQLAlchemy(app)
# encriptación del sistema de logeo
app.config['SECRET_KEY']='MATcomerce159753%&ñ'
bcrypt = Bcrypt(app)


from Tienda.Administrador import routes