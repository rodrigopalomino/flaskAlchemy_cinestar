from db.connection import db

class Pelicula(db.Model):

  __tablename__ = "pelicula"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  Titulo = db.Column(db.String(80))
  FechaEstreno = db.Column(db.String(10))
  Director = db.Column(db.String(50))
  Generos = db.Column(db.String(10))
  idClasificacion =  db.Column(db.Integer)
  idEstado = db.Column(db.Integer)
  Duracion = db.Column(db.String(3))
  Link =  db.Column(db.String(20))
  Reparto = db.Column(db.Text)
  Sinopsis  = db.Column(db.Text)