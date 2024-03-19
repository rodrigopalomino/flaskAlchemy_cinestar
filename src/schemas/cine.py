from flask_marshmallow import Marshmallow

ma = Marshmallow()

class CineSchema(ma.Schema):
    class Meta:
        fields = ("id", "RazonSocial", "Salas", "idDistrito", "Direccion", "Telefonos")

genero_schema = CineSchema()
generos_schema = CineSchema(many=True)
