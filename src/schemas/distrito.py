from flask_marshmallow import Marshmallow

ma = Marshmallow()

class DistritoSchema(ma.Schema):
    class Meta:
        fields = ("id", "Detalle")

distrito_schema = DistritoSchema()
distritos_schema = DistritoSchema(many=True)
