from flask import Flask
from flask_cors import CORS
from app import db
from app.routes.itemCarro import itemCarro_bp
from app.routes.productos import productos_bp
from app.routes.carroCompras import carroCompras_bp
from app.routes.pedido import pedido_bp


def create_app():
    app = Flask(__name__)

    # Configuración de conexión a PostgreSQL
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:1001204488@localhost:5432/e_commerce_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar extensiones
    db.init_app(app)
    CORS(app)  # Habilita CORS para acceso desde el frontend

    # Registrar los blueprints
    app.register_blueprint(productos_bp, url_prefix='/productos')
    app.register_blueprint(itemCarro_bp, url_prefix='/item_carro')
    app.register_blueprint(carroCompras_bp, url_prefix='/carro_compras')
    app.register_blueprint(pedido_bp, url_prefix='/pedido')

    return app


app = create_app()

# Solo se ejecuta si corres directamente este archivo
if __name__ == '__main__':
    app.run(debug=True)