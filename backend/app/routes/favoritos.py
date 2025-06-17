from flask import Blueprint, request, jsonify
from app import db
from app.models import Favoritos, Productos, Usuarios, Categoria, Marca, Talla

favoritos_bp = Blueprint('favoritos', __name__)

@favoritos_bp.route('/obtener-favoritos/<int:idUsuario>', methods=['GET'])
def obtener_favoritos_usuario(idUsuario):
    favoritos = Favoritos.query.filter_by(idUsuario=idUsuario).all()
    resultado = []

    for item in favoritos:
        producto = Productos.query.get_or_404(item.idProductos)
        categoria = Categoria.query.get_or_404(producto.idCategoria)
        marca = Marca.query.get_or_404(producto.idMarca)
        talla = Talla.query.get_or_404(producto.idTalla)
        resultado.append({
            'id': item.id,
            'idProductos': item.idProductos,
            'nombre': producto.nombre,
            'descripcion': producto.descripcion,
            'precio': producto.precio,
            'stock': producto.stock,
            'imagenPrin': producto.imagenPrin,
            'imagenesDet': producto.imagenesDet,
            'categoria': categoria.categoria,
            'marca': marca.marca,
            'talla': talla.talla,
            'idUsuario': item.idUsuario
        })

    return jsonify(resultado)


@favoritos_bp.route('//', methods=['GET'])
def obtener_favoritos():
    favoritos = Favoritos.query.all()
    resultado = []

    for item in favoritos:
        producto = Productos.query.get_or_404(item.idProductos)
        categoria = Categoria.query.get_or_404(producto.idCategoria)
        marca = Marca.query.get_or_404(producto.idMarca)
        talla = Talla.query.get_or_404(producto.idTalla)
        resultado.append({
            'id': item.id,
            'idProductos': item.idProductos,
            'nombre': producto.nombre,
            'descripcion': producto.descripcion,
            'precio': producto.precio,
            'stock': producto.stock,
            'imagenPrin': producto.imagenPrin,
            'imagenesDet': producto.imagenesDet,
            'categoria': categoria.categoria,
            'marca': marca.marca,
            'talla': talla.talla,
            'idUsuario': item.idUsuario
        })

    return jsonify(resultado)


@favoritos_bp.route('//<int:id>', methods=['GET'])
def buscar_favorito(id):
    favorito = Favoritos.query.get_or_404(id)
    resultado = []

    producto = Productos.query.get_or_404(favorito.idProductos)
    categoria = Categoria.query.get_or_404(producto.idCategoria)
    marca = Marca.query.get_or_404(producto.idMarca)
    talla = Talla.query.get_or_404(producto.idTalla)
    resultado.append({
        'id': favorito.id,
            'idProductos': favorito.idProductos,
            'nombre': producto.nombre,
            'descripcion': producto.descripcion,
            'precio': producto.precio,
            'stock': producto.stock,
            'imagenPrin': producto.imagenPrin,
            'imagenesDet': producto.imagenesDet,
            'categoria': categoria.categoria,
            'marca': marca.marca,
            'talla': talla.talla,
            'idUsuario': favorito.idUsuario
        })

    return jsonify(resultado)


@favoritos_bp.route('/', methods=['POST'])
def crear_favorito():
    data = request.get_json()
    nuevo_favorito = Favoritos(
        idUsuario = int(data['idUsuario']),
        idProductos = int(data['idProductos'])
    )
    db.session.add(nuevo_favorito)
    db.session.commit()
    return jsonify({'mensaje': 'Favorito creado exitosamente'}), 201



@favoritos_bp.route('//<int:id>', methods=['PUT'])
def actualizar_favorito(id):
    favorito = Favoritos.query.get_or_404(id)
    data = request.get_json()
    favorito.idUsuario = data['idUsuario']
    favorito.idProductos = data['idProductos']
    db.session.commit()
    return jsonify({'mensaje': 'Favorito actualizado'})



@favoritos_bp.route('//<int:id>', methods=['DELETE'])
def eliminar_favorito(id):
    favorito = Favoritos.query.get_or_404(id)
    db.session.delete(favorito)
    db.session.commit()
    return jsonify({'mensaje': 'Favorito eliminado'})