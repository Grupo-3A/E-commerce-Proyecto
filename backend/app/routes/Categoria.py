from flask import Blueprint, request, jsonify
from app import db
from app.models import Categoria

categoria_bp = Blueprint('categoria', __name__)

@categoria_bp.route('/', methods=['GET'])
def obtener_categorias():
    categorias = Categoria.query.all()
    resultado = []

    for item in categorias:
        resultado.append({
            'id': item.id,
            'categoria': item.categoria
        })


    return jsonify(resultado)


@categoria_bp.route('//<int:id>', methods=['GET'])
def buscar_categoria(id):
    categoria = Categoria.query.get_or_404(id)
    resultado = []

    resultado.append({
        'id': categoria.id,
        'categoria': categoria.categoria
    })

    return jsonify(resultado)


@categoria_bp.route('/', methods=['POST'])
def crear_categoria():
    data = request.get_json()
    nueva_categoria = Categoria(
        categoria=data['categoria']
    )
    db.session.add(nueva_categoria)
    db.session.commit()
    return jsonify({'mensaje': 'Categoria creada exitosamente'}), 201



@categoria_bp.route('//<int:id>', methods=['PUT'])
def actualizar_categoria(id):
    categoria = Categoria.query.get_or_404(id)
    data = request.get_json()
    categoria.categoria = data['categoria']
    db.session.commit()
    return jsonify({'mensaje': 'Categoria actualizada'})



@categoria_bp.route('//<int:id>', methods=['DELETE'])
def eliminar_categoria(id):
    categoria = Categoria.query.get_or_404(id)
    db.session.delete(categoria)
    db.session.commit()
    return jsonify({'mensaje': 'Categoria eliminada'})