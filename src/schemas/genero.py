from flask_marshmallow import Marshmallow

ma = Marshmallow()


class GeneroSchema(ma.Schema):
    class Meta:
        fields = ("id", "Detalle")


genero_schema = GeneroSchema()
generos_schema = GeneroSchema(many=True)
