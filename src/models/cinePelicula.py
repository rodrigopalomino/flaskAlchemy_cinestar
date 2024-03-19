from db.connection import db

class CinePelicula(db.Model):

    __tablename__ = "cinepelicula"

    idCine = db.Column(db.Integer, db.ForeignKey("cine.id"), primary_key=True)  # Clave foránea que hace referencia al id de la tabla Cine
    idPelicula = db.Column(db.Integer, db.ForeignKey("pelicula.id"), primary_key=True)  # Clave foránea que hace referencia al id de la tabla Pelicula
    Sala = db.Column(db.Integer)  # Número de sala donde se proyecta la película
    Horarios = db.Column(db.String(150))  # Horarios de proyección de la película en formato de cadena

    # Definir la relación con la tabla Cine
    cine = db.relationship("Cine", backref=db.backref("peliculas_cine", lazy=True))

    # Definir la relación con la tabla Pelicula
    pelicula = db.relationship("Pelicula", backref=db.backref("cines_pelicula", lazy=True))
