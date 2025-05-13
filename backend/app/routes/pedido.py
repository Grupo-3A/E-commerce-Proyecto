from flask import Blueprint, request, jsonify
from app import db
from app.models import Pedido, CarroCompras

pedido_bp = Blueprint('pedido', __name__)

@pedido_bp.route('/', methods=['GET'])
def obtener_pedidos():
    pedido = Pedido.query.all()
    resultado = []

    for item in pedido:
        carroCompras = CarroCompras.query.get_or_404(item.idCarroCom)
        resultado.append({
            'id': item.id,
            'nombreUsuario': item.nombreUsuario,
            'email': item.email,
            'telefono': item.telefono,
            'direccion': item.direccion,
            'detalleDireccion': item.detalleDireccion,
            'cedula': item.cedula,
            'idCarroCom': item.idCarroCom,
            'subtotal': carroCompras.subtotal
        })

    return jsonify(resultado)


@pedido_bp.route('//<int:id>', methods=['GET'])
def buscar_pedido(id):
    pedido = Pedido.query.get_or_404(id)
    resultado = []

    carroCompras = CarroCompras.query.get_or_404(pedido.idCarroCom)
    resultado.append({
        'id': pedido.id,
        'nombreUsuario': pedido.nombreUsuario,
        'email': pedido.email,
        'telefono': pedido.telefono,
        'direccion': pedido.direccion,
        'detalleDireccion': pedido.detalleDireccion,
        'cedula': pedido.cedula,
        'idCarroCom': pedido.idCarroCom,
        'subtotal': carroCompras.subtotal
    })

    return jsonify(resultado)


@pedido_bp.route('/', methods=['POST'])
def crear_pedido():
    data = request.get_json()
    nuevo_pedido = Pedido(
        nombreUsuario=data['nombreUsuario'],
        email=data['email'],
        telefono=data['telefono'],
        direccion=data['direccion'],
        detalleDireccion=data['detalleDireccion'],
        cedula=data['cedula'],
        idCarroCom=int(data['idCarroCom'])
    )
    db.session.add(nuevo_pedido)
    db.session.commit()
    return jsonify({'mensaje': 'Pedido creado exitosamente'}), 201



@pedido_bp.route('//<int:id>', methods=['PUT'])
def actualizar_pedido(id):
    pedido = Pedido.query.get_or_404(id)
    data = request.get_json()
    pedido.nombreUsuario = data['nombreUsuario']
    pedido.email= data['email']
    pedido.telefono = data['telefono']
    pedido.direccion = data['direccion']
    pedido.detalleDireccion = data.get('detalleDireccion')
    pedido.cedula = data['cedula']
    pedido.idCarroCom = data['idCarroCom']
    db.session.commit()
    return jsonify({'mensaje': 'Pedido actualizado'})



@pedido_bp.route('//<int:id>', methods=['DELETE'])
def eliminar_pedido(id):
    pedido = Pedido.query.get_or_404(id)
    db.session.delete(pedido)
    db.session.commit()
    return jsonify({'mensaje': 'Pedido eliminado'})