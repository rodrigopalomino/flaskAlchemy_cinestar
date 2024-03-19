from flask_marshmallow import Marshmallow

ma = Marshmallow()


class CineTarifaSchema(ma.Schema):
    class Meta:
        fields = ("DiasSemana", "Precio")
