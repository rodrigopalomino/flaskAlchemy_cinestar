from db.connection import db

class Cine(db.Model):
    
    __tablename__ = "cine"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    RazonSocial = db.Column(db.String(30))
    Salas = db.Column(db.Integer)
    idDistrito = db.Column(db.Integer, db.ForeignKey("distrito.id"), nullable=True)
    Direccion = db.Column(db.String(100))
    Telefonos = db.Column(db.String(20))

    distrito = db.relationship("Distrito", backref=db.backref("cines", lazy=True))
