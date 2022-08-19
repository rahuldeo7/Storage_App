from contextlib import nullcontext
from uuid import uuid4
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
db1 = SQLAlchemy()

def get_uuid():
    return uuid4().hex

class ClientUser(db.Model):
    __tablename__ = "users-client"
    id = db.Column(db.String(32), primary_key = True, unique = True, default = get_uuid)
    email = db.Column(db.String(345), unique=True)
    password = db.Column(db.Text, nullable=False)
    user_type =  db.Column(db.Text, nullable = False)



class DevUser(db1.Model):
    __tablename__ = "users-dev"
    id = db.Column(db.String(32), primary_key = True, unique = True, default = get_uuid)
    email = db.Column(db.String(345), unique=True)
    password = db.Column(db.Text, nullable=False)
    user_type =  db.Column(db.Text, nullable = False)