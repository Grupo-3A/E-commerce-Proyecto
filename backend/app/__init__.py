from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    # Configuraciones
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:1001204488@localhost/e_commerce_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)

    # Importar modelos para que Flask-Migrate los vea
    from . import models

    return app