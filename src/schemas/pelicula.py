from flask_marshmallow import Marshmallow

ma = Marshmallow()


class PeliculaSchema(ma.Schema):
    class Meta:
        fields = ("id", "Titulo", "FechaEstreno", "Director", "Generos",
                  "idClasificacion", "idEstado", "Duracion", "Link", "Reparto", "Sinopsis", "Geneross", "FechaEstrenoss")


class PeliculasSchema(ma.Schema):
    class Meta:
        fields = ("id", "Titulo", "Sinopsis", "Link")
