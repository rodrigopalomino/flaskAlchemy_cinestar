from flask_marshmallow import Marshmallow

ma = Marshmallow()

class CinePeliculaSchema(ma.Schema):
    class Meta:
        fields = ("idCine","idPelicula","Sala","Horarios")

CinePelicula_schema = CinePeliculaSchema()
CinePelicula_schema = CinePeliculaSchema(many=True)
