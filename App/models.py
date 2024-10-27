from .extentions import db
from sqlalchemy import Column,Integer,String,PickleType,Boolean
from flask_sqlalchemy import SQLAlchemy

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(20),unique=True,nullable=False)
    age = db.Column(db.Integer,default=15)
    gender = db.Column(db.Boolean,default=1)
    

