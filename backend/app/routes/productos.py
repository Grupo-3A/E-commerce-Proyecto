from flask import Blueprint, request, jsonify
from app import db
from app.models import Productos

productos_bp = Blueprint('productos', __name__)

# GET: Obtener todos los productos
@productos_bp.route('//<int:id>', methods=['GET'])
def buscar_producto():
    producto = Productos.query.get_or_404(id)
    resultado = []

    resultado.append({
    'id': producto.id,
    'nombre': producto.nombre,
    'descripcion': producto.descripcion,
    'precio': producto.precio,
    'stock': producto.stock,
    'imagen': producto.imagen
    })

    return jsonify(resultado)


# GET: Buscar un producto
@productos_bp.route('/', methods=['GET'])
def obtener_productos():
    productos = Productos.query.all()
    return jsonify([{
        'id': p.id,
        'nombre': p.nombre,
        'descripcion': p.descripcion,
        'precio': p.precio,
        'stock': p.stock,
        'imagen': p.imagen
    } for p in productos])


# POST: Crear un nuevo producto
@productos_bp.route('/', methods=['POST'])
def crear_producto():
    data = request.get_json()
    nuevo_producto = Productos(
        nombre=data['nombre'],
        descripcion=data['descripcion'],
        precio=float(data['precio']),
        stock=int(data['stock']),
        imagen=data.get('imagen')
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
    producto.imagen = data.get('imagen')
    db.session.commit()
    return jsonify({'mensaje': 'Producto actualizado'})

# DELETE: Eliminar un producto
@productos_bp.route('//<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    producto = Productos.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    return jsonify({'mensaje': 'Producto eliminado'})