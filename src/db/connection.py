from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Configuración de la base de datos
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root@localhost:3306/cinestar'
SQLALCHEMY_TRACK_MODIFICATIONS = False
