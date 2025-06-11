from flask import Blueprint, request, jsonify
from app import db
from app.models import Productos, Categoria, Marca, Talla

productos_bp = Blueprint('productos', __name__)

# GET: Buscar un producto
@productos_bp.route('//<int:id>', methods=['GET'])
def buscar_producto(id):
    producto = Productos.query.get_or_404(id)
    categoria = Categoria.query.get_or_404(producto.idCategoria)
    marca = Marca.query.get_or_404(producto.idMarca)
    talla = Talla.query.get_or_404(producto.idTalla)
    resultado = []

    resultado.append({
    'id': producto.id,
    'nombre': producto.nombre,
    'descripcion': producto.descripcion,
    'precio': producto.precio,
    'stock': producto.stock,
    'imagenPrin': producto.imagenPrin,
    'imagenesDet': producto.imagenesDet,
    'categoria': categoria.categoria,
    'marca': marca.marca,
    'talla': talla.talla
    })

    return jsonify(resultado)


# GET: Obtener todos los productos
@productos_bp.route('/', methods=['GET'])
def obtener_productos():
    resultado = []
    productos = Productos.query.all()

    for item in productos:
        categoria = Categoria.query.get_or_404(item.idCategoria)
        marca = Marca.query.get_or_404(item.idMarca)
        talla = Talla.query.get_or_404(item.idTalla)

        resultado.append({
            'id': item.id,
            'nombre': item.nombre,
            'descripcion': item.descripcion,
            'precio': item.precio,
            'stock': item.stock,
            'imagenPrin': item.imagenPrin,
            'imagenesDet': item.imagenesDet,
            'categoria': categoria.categoria,
            'marca': marca.marca,
            'talla': talla.talla
            })

    return jsonify(resultado)


# GET: Obtener todos los productos por Categoria
@productos_bp.route('/categoria/<int:idCategoria>', methods=['GET'])
def obtener_productos_categoria(idCategoria):
    resultado = []
    productos = Productos.query.filter_by(idCategoria=idCategoria).all()

    for item in productos:
        categoria = Categoria.query.get_or_404(item.idCategoria)
        marca = Marca.query.get_or_404(item.idMarca)
        talla = Talla.query.get_or_404(item.idTalla)

        resultado.append({
            'id': item.id,
            'nombre': item.nombre,
            'descripcion': item.descripcion,
            'precio': item.precio,
            'stock': item.stock,
            'imagenPrin': item.imagenPrin,
            'imagenesDet': item.imagenesDet,
            'categoria': categoria.categoria,
            'marca': marca.marca,
            'talla': talla.talla
            })

    return jsonify(resultado)


# GET: Obtener todos los productos por Marca
@productos_bp.route('/marca/<int:idMarca>', methods=['GET'])
def obtener_productos_marca(idMarca):
    resultado = []
    productos = Productos.query.filter_by(idMarca=idMarca).all()

    for item in productos:
        categoria = Categoria.query.get_or_404(item.idCategoria)
        marca = Marca.query.get_or_404(item.idMarca)
        talla = Talla.query.get_or_404(item.idTalla)

        resultado.append({
            'id': item.id,
            'nombre': item.nombre,
            'descripcion': item.descripcion,
            'precio': item.precio,
            'stock': item.stock,
            'imagenPrin': item.imagenPrin,
            'imagenesDet': item.imagenesDet,
            'categoria': categoria.categoria,
            'marca': marca.marca,
            'talla': talla.talla
            })

    return jsonify(resultado)


# POST: Crear un nuevo producto
@productos_bp.route('/', methods=['POST'])
def crear_producto():
    data = request.get_json()
    nuevo_producto = Productos(
        nombre=data['nombre'],
        descripcion=data['descripcion'],
        precio=float(data['precio']),
        stock=int(data['stock']),
        imagenPrin=data.get('imagenPrin'),
        imagenesDet=data.get('imagenesDet'),
        idCategoria=int(data['idCategoria']),
        idMarca=int(data['idMarca']),
        idTalla=int(data['idTalla'])
    )
    db.session.add(nuevo_producto)
    db.session.commit()
    return jsonify({'mensaje': 'Producto creado exitosamente'}), 201


# PUT: Actualizar un producto
@productos_bp.route('//<int:id>', methods=['PUT'])
def actualizar_producto(id):
    producto = Productos.query.get_or_404(id)
    data = request.get_json()
    producto.nombre = data['nombre']
    producto.descripcion = data['descripcion']
    producto.precio = data['precio']
    producto.stock = data['stock']
    producto.imagenPrin = data.get('imagenPrin')
    producto.imagenesDet = data.get('imagenesDet')
    producto.idCategoria = data['idCategoria']
    producto.idMarca = data['idMarca']
    producto.idTalla = data['idTalla']
    db.session.commit()
    return jsonify({'mensaje': 'Producto actualizado'})


# DELETE: Eliminar un producto
@productos_bp.route('//<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    producto = Productos.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    return jsonify({'mensaje': 'Producto eliminado'})