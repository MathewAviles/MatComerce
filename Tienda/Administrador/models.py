from Tienda import db, app
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
import os


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=False)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(255), unique=False)
    profile: Mapped[str] = mapped_column(String(255), unique=False, default='profile.jpg')


    def __repr__(self):
        return '<User %r>' % self.username
    
with app.app_context():
    db.create_all()