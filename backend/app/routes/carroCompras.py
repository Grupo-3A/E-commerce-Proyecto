from flask import Blueprint, request, jsonify
from app import db
from app.models import CarroCompras, Productos

carroCompras_bp = Blueprint('carro_compras', __name__)

@carroCompras_bp.route('/', methods=['GET'])
def obtener_carrosCom():
    carrosCom = CarroCompras.query.all()
    resultado = []

    for item in carrosCom:
        resultado.append({
            'id': item.id,
            'idUsuario': item.idUsuario,
            'subtotal': item.subtotal
        })


    return jsonify(resultado)


@carroCompras_bp.route('//<int:id>', methods=['GET'])
def buscar_carroCom(id):
    carroCom = CarroCompras.query.get_or_404(id)
    resultado = []

    resultado.append({
        'idUsuario': carroCom.idUsuario,
        'subtotal': carroCom.subtotal
    })

    return jsonify(resultado)


@carroCompras_bp.route('/', methods=['POST'])
def crear_carroCom():
    data = request.get_json()
    nuevo_carroCom = CarroCompras(
        idUsuario=int(data['idUsuario']),
        subtotal=float(data['subtotal'])
    )
    db.session.add(nuevo_carroCom)
    db.session.commit()
    return jsonify({'mensaje': 'Carro Compras creado exitosamente'}), 201



@carroCompras_bp.route('//<int:id>', methods=['PUT'])
def actualizar_carroCom(id):
    carroCom = CarroCompras.query.get_or_404(id)
    data = request.get_json()
    carroCom.subtotal = data['subtotal']
    carroCom.idUsuario = data['idUsuario']
    db.session.commit()
    return jsonify({'mensaje': 'Carro Compras actualizado'})



@carroCompras_bp.route('//<int:id>', methods=['DELETE'])
def eliminar_carroCom(id):
    carroCom = CarroCompras.query.get_or_404(id)
    db.session.delete(carroCom)
    db.session.commit()
    return jsonify({'mensaje': 'Carro Compras eliminado'})