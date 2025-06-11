from flask import Flask
from flask_cors import CORS
from app import db
from app.routes.Categoria import categoria_bp
from app.routes.favoritos import favoritos_bp
from app.routes.itemCarro import itemCarro_bp
from app.routes.productos import productos_bp
from app.routes.carroCompras import carroCompras_bp
from app.routes.pedido import pedido_bp
from app.routes.usuarios import usuario_bp
from app.routes.Marca import marca_bp
from app.routes.Talla import talla_bp
from flask_jwt_extended import JWTManager


def create_app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = '1001204488'
    jwt = JWTManager(app)

    # Configuración de conexión a PostgreSQL
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:1001204488@localhost:5432/e_commerce_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar extensiones
    db.init_app(app)
    CORS(app, supports_credentials=True)  # Habilita CORS para acceso desde el frontend

    # Registrar los blueprints
    app.register_blueprint(productos_bp, url_prefix='/productos')
    app.register_blueprint(itemCarro_bp, url_prefix='/item_carro')
    app.register_blueprint(carroCompras_bp, url_prefix='/carro_compras')
    app.register_blueprint(pedido_bp, url_prefix='/pedido')
    app.register_blueprint(usuario_bp, url_prefix='/usuarios')
    app.register_blueprint(favoritos_bp, url_prefix='/favoritos')
    app.register_blueprint(categoria_bp, url_prefix='/categoria')
    app.register_blueprint(marca_bp, url_prefix='/marca')
    app.register_blueprint(talla_bp, url_prefix='/talla')

    return app


app = create_app()

# Solo se ejecuta si corres directamente este archivo
if __name__ == '__main__':
    app.run(debug=True)