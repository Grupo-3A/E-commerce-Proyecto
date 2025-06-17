from flask import Blueprint, request, jsonify
from app import db
from app.models import Talla

talla_bp = Blueprint('talla', __name__)

@talla_bp.route('/', methods=['GET'])
def obtener_talla():
    tallas = Talla.query.all()
    resultado = []

    for item in tallas:
        resultado.append({
            'id': item.id,
            'talla': item.talla
        })


    return jsonify(resultado)


@talla_bp.route('//<int:id>', methods=['GET'])
def buscar_talla(id):
    talla = Talla.query.get_or_404(id)
    resultado = []

    resultado.append({
        'id': talla.id,
        'talla': talla.talla
    })

    return jsonify(resultado)


@talla_bp.route('/', methods=['POST'])
def crear_talla():
    data = request.get_json()
    nueva_talla = Talla(
        talla=data['talla']
    )
    db.session.add(nueva_talla)
    db.session.commit()
    return jsonify({'mensaje': 'Talla creada exitosamente'}), 201



@talla_bp.route('//<int:id>', methods=['PUT'])
def actualizar_talla(id):
    talla = Talla.query.get_or_404(id)
    data = request.get_json()
    talla.talla = data['talla']
    db.session.commit()
    return jsonify({'mensaje': 'Talla actualizada'})



@talla_bp.route('//<int:id>', methods=['DELETE'])
def eliminar_talla(id):
    talla = Talla.query.get_or_404(id)
    db.session.delete(talla)
    db.session.commit()
    return jsonify({'mensaje': 'Talla eliminada'})