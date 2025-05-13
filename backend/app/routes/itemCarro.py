from flask import Blueprint, request, jsonify
from app import db
from app.models import ItemCarro, Productos, CarroCompras

itemCarro_bp = Blueprint('item_carro', __name__)

@itemCarro_bp.route('/', methods=['GET'])
def obtener_itemCar():
    items = ItemCarro.query.all()
    resultado = []

    for item in items:
        producto = Productos.query.get_or_404(item.idProductos)
        resultado.append({
            'id': item.id,
            'idProductos': item.idProductos,
            'nombre': producto.nombre,
            'descripcion': producto.descripcion,
            'precio': producto.precio,
            'stock': producto.stock,
            'imagen': producto.imagen,
            'idCarro': item.idCarro,
            'cantidad': item.cantidad
        })

    return jsonify(resultado)


@itemCarro_bp.route('//<int:id>', methods=['GET'])
def buscar_itemCar(id):
    itemCar = ItemCarro.query.get_or_404(id)
    resultado = []

    producto = Productos.query.get_or_404(itemCar.idProductos)
    resultado.append({
    'id': itemCar.id,
    'idProductos': itemCar.idProductos,
    'nombre': producto.nombre,
    'descripcion': producto.descripcion,
    'precio': producto.precio,
    'stock': producto.stock,
    'imagen': producto.imagen,
    'idCarro': itemCar.idCarro,
    'cantidad': itemCar.cantidad
    })

    return jsonify(resultado)



@itemCarro_bp.route('/por-carro/<int:idCarro>', methods=['GET'])
def obtener_items_carro_compras(idCarro):
    items = ItemCarro.query.filter_by(idCarro=idCarro).all()
    resultado = []

    for item in items:
        producto = Productos.query.get_or_404(item.idProductos)
        resultado.append({
            'id': item.id,
            'idProductos': item.idProductos,
            'nombre': producto.nombre,
            'descripcion': producto.descripcion,
            'precio': producto.precio,
            'stock': producto.stock,
            'imagen': producto.imagen,
            'idCarro': item.idCarro,
            'cantidad': item.cantidad
        })

    return jsonify(resultado)



@itemCarro_bp.route('/', methods=['POST'])
def crear_itemCar():
    data = request.get_json()
    nuevo_itemCar = ItemCarro(
        idProductos=int(data['idProductos']),
        idCarro=int(data['idCarro']),
        cantidad=int(data['cantidad'])
    )
    db.session.add(nuevo_itemCar)
    db.session.commit()
    return jsonify({'mensaje': 'Item Carro creado exitosamente'}), 201



@itemCarro_bp.route('//<int:id>', methods=['PUT'])
def actualizar_itemCar(id):
    itemCar = ItemCarro.query.get_or_404(id)
    data = request.get_json()
    itemCar.idProductos = data['idProductos']
    itemCar.idCarro = data['idCarro']
    itemCar.cantidad = data['cantidad']
    db.session.commit()
    return jsonify({'mensaje': 'Item Carro actualizado'})



@itemCarro_bp.route('//<int:id>', methods=['DELETE'])
def eliminar_itemCar(id):
    itemCar = ItemCarro.query.get_or_404(id)
    db.session.delete(itemCar)
    db.session.commit()
    return jsonify({'mensaje': 'Item Carro eliminado'})