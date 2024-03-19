from db.connection import db

class Genero(db.Model):

    __tablename__ = "genero"

    id = db.Column(db.Integer, primary_key=True)
    Detalle = db.Column(db.String(30), unique=True, nullable=True)

    def __init__(self, Detalle):
        self.Detalle = Detalle
