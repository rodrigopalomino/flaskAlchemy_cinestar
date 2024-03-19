from db.connection import db

class Distrito(db.Model):

  __tablename__ = "distrito"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  Detalle = db.Column(db.String(30), nullable=True, unique=True)
