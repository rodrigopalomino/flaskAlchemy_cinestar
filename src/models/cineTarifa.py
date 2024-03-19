from db.connection import db


class CineTarifa(db.Model):

    __tablename__ = "cinetarifa"

    idCine = db.Column(db.Integer, db.ForeignKey("cine.id"), primary_key=True)
    # Días de la semana para los que se aplica la tarifa
    DiasSemana = db.Column(db.String(80), primary_key=True)
    Precio = db.Column(db.Numeric(5, 2))  # Precio de la tarifa

    # Definir la relación con la tabla Cine
    cine = db.relationship(
        "Cine", backref=db.backref("tarifas_cine", lazy=True))
