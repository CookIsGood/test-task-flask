from conn_db import db


class Animal(db.Model):
    __tablename__ = 'animal'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    type = db.Column(db.String(50), unique=False, nullable=False)
    speed = db.Column(db.Integer, unique=False, nullable=False)
    predator = db.Column(db.Boolean, unique=False, nullable=False)


