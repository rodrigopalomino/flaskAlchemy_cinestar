from datetime import datetime
from flask import Flask, jsonify
from flask_marshmallow import Marshmallow
import locale
from datetime import datetime
from flask_cors import CORS

# modulos propios
from db.connection import db
from models.__init__ import Cine, Distrito, Pelicula, Genero, CineTarifa, CinePelicula
from schemas.__init__ import CineSchema, PeliculasSchema, PeliculaSchema, GeneroSchema, CineTarifaSchema, DistritoSchema


app = Flask(__name__)
CORS(app)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/cinestar'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialización de SQLAlchemy y Marshmallow
db.init_app(app)
ma = Marshmallow(app)

# Creación de todas las tablas en la base de datos
with app.app_context():
    db.create_all()


# Cines
@app.route("/cines", methods=["GET"])
def getCines():
    # Realiza la consulta utilizando SQLAlchemy
    query = db.session.query(Cine, Distrito.Detalle).join(
        Distrito, Cine.idDistrito == Distrito.id)

    # Ejecuta la consulta y obtén los resultados
    results = query.all()

    # Serializa los resultados utilizando el esquema adecuado
    output = []
    for cine, detalle in results:
        cine_data = {
            "id": cine.id,
            "RazonSocial": cine.RazonSocial,
            "Salas": cine.Salas,
            "idDistrito": cine.idDistrito,  # Usamos cine.idDistrito
            "Direccion": cine.Direccion,
            "Telefonos": cine.Telefonos,
            "Detalle": detalle  # Usamos detalle en lugar de detalle.Detalle
        }
        output.append(cine_data)

    # Devuelve los resultados serializados como JSON
    return jsonify(output), 200


@app.route("/cines/<cine_id>")
def getCine(cine_id):

    queryCine = Cine.query.filter_by(id=cine_id).one()
    cine = CineSchema().dump(queryCine)

    queryDistrito = Distrito.query.filter_by(id=queryCine.idDistrito).one()
    distrito = DistritoSchema().dump(queryDistrito)

    cine["Detalle"] = distrito["Detalle"]  # type: ignore

    return cine


@app.route("/cines/<cine_id>/tarifas")
def getCineTarifas(cine_id):

    query = CineTarifa.query.filter_by(idCine=cine_id).all()
    tarifas = CineTarifaSchema(many=True).dump(query)

    return tarifas


@app.route("/cines/<cine_id>/peliculas")
def getCinePeliculas(cine_id):

    query = db.session.query(CinePelicula, Pelicula.Titulo).join(
        Pelicula, CinePelicula.idPelicula == Pelicula.id).filter(CinePelicula.idCine == cine_id).all()

    output = []

    for cine, Titulo in query:
        output.append({
            "Titulo": Titulo,
            "Horarios": cine.Horarios
        })

    return output


# Peliculas
@app.route("/peliculas/<id>")
def getPeliculas(id):

    id = "1" if id == "cartelera" else "2" if id == "estrenos" else ""

    peliculas = Pelicula.query.filter_by(idEstado=id).all()

    peliculasJson = PeliculasSchema(many=True).dump(peliculas)

    return peliculasJson


@app.route("/pelicula/<pelicula_id>")
def getPelicula(pelicula_id):

    queryPelicula = Pelicula.query.filter_by(id=pelicula_id).all()
    pelicula = PeliculaSchema(many=True).dump(queryPelicula)

    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    fechaEstreno = datetime.strptime(pelicula[0]["FechaEstreno"], "%Y/%m/%d")
    fecha_estreno_texto = fechaEstreno.strftime("%A %d de %B del %Y")

    generos = ""
    listGeneros = pelicula[0]["Generos"].split(",")
    for idGenero in listGeneros:
        queryGenero = Genero.query.filter_by(id=idGenero)
        genero = GeneroSchema(many=True).dump(queryGenero)
        generos += genero[0]["Detalle"] + " ,"

    pelicula[0]["Geneross"] = generos
    pelicula[0]["FechaEstrenoss"] = fecha_estreno_texto

    return pelicula[0]


if __name__ == "__main__":
    app.run(debug=True)
