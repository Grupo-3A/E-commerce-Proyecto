from flask import Blueprint, request, jsonify
from app import db
from app.models import Marca

marca_bp = Blueprint('marca', __name__)

@marca_bp.route('/', methods=['GET'])
def obtener_marca():
    marcas = Marca.query.all()
    resultado = []

    for item in marcas:
        resultado.append({
            'id': item.id,
            'marca': item.marca
        })


    return jsonify(resultado)


@marca_bp.route('//<int:id>', methods=['GET'])
def buscar_marca(id):
    marca = Marca.query.get_or_404(id)
    resultado = []

    resultado.append({
        'id': marca.id,
        'categoria': marca.marca
    })

    return jsonify(resultado)


@marca_bp.route('/', methods=['POST'])
def crear_marca():
    data = request.get_json()
    nueva_marca = Marca(
        marca=data['marca']
    )
    db.session.add(nueva_marca)
    db.session.commit()
    return jsonify({'mensaje': 'Marca creada exitosamente'}), 201



@marca_bp.route('//<int:id>', methods=['PUT'])
def actualizar_marca(id):
    marca = Marca.query.get_or_404(id)
    data = request.get_json()
    marca.marca = data['marca']
    db.session.commit()
    return jsonify({'mensaje': 'Marca actualizada'})



@marca_bp.route('//<int:id>', methods=['DELETE'])
def eliminar_marca(id):
    marca = Marca.query.get_or_404(id)
    db.session.delete(marca)
    db.session.commit()
    return jsonify({'mensaje': 'Marca eliminada'})