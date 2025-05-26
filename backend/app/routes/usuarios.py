from flask import Blueprint, request, jsonify
from app import db
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.models import Usuarios

usuario_bp = Blueprint('usuarios', __name__)

@usuario_bp.route('/', methods=['GET'])
def obtener_usuarios():
    usuarios = Usuarios.query.all()
    resultado = []

    for item in usuarios:
        resultado.append({
            'id': item.id,
            'nombreUsu': item.nombreUsu,
            'password': item.password,
            'email': item.email,
            'telefono': item.telefono,
            'direccion': item.direccion,
            'detDireccion': item.detDireccion,
            'cedula': item.cedula
        })

    return jsonify(resultado)


@usuario_bp.route('//<int:id>', methods=['GET'])
def buscar_usuario(id):
    usuario = Usuarios.query.get_or_404(id)
    resultado = []

    resultado.append({
            'id': usuario.id,
            'nombreUsu': usuario.nombreUsu,
            'password': usuario.password,
            'email': usuario.email,
            'telefono': usuario.telefono,
            'direccion': usuario.direccion,
            'detDireccion': usuario.detDireccion,
            'cedula': usuario.cedula
        })
    return jsonify(resultado)


@usuario_bp.route('/', methods=['POST'])
def crear_usuario():
    data = request.get_json()
    if Usuarios.query.filter_by(email=data['email']).first():
        return jsonify({'mensaje': 'El correo ya está registrado'}), 400

    nuevo_usuario = Usuarios(
        nombreUsu=data['nombreUsu'],
        email=data['email'],
        telefono=data['telefono'],
        direccion=data['direccion'],
        detDireccion=data['detDireccion'],
        cedula=data['cedula']
    )
    nuevo_usuario.set_password(data['password'])

    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({'mensaje': 'Usuario creado exitosamente'}), 201



@usuario_bp.route('//<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    usuario = Usuarios.query.get_or_404(id)
    data = request.get_json()
    usuario.nombreUsu = data['nombreUsu']
    usuario.password = data['password']
    usuario.email= data['email']
    usuario.telefono = data['telefono']
    usuario.direccion = data['direccion']
    usuario.detDireccion = data.get('detDireccion')
    usuario.cedula = data['cedula']
    db.session.commit()
    return jsonify({'mensaje': 'Usuario actualizado'})



@usuario_bp.route('//<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    usuario = Usuarios.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return jsonify({'mensaje': 'Usuario eliminado'})


@usuario_bp.route('/login', methods=['POST'])
def login():
    datos = request.get_json()

    email = datos.get('email')
    contraseña = datos.get('password')

    usuario = Usuarios.query.filter_by(email=email).first()

    if usuario and usuario.check_password(contraseña):
        access_token = create_access_token(identity=usuario.id)

        return jsonify({
            'mensaje': 'Login exitoso',
            'token': access_token,
            'usuario': {
                'id': usuario.id,
                'nombre': usuario.nombreUsu,
                'email': usuario.email
            }
        }), 200
    else:
        return jsonify({'mensaje': 'Credenciales incorrectas'}), 401


@usuario_bp.route('/perfil', methods=['GET'])
@jwt_required()
def perfil():
    usuario_id = get_jwt_identity()
    usuario = Usuarios.query.get(usuario_id)
    return jsonify({
        'nombreUsu': usuario.nombreUsu,
        'email': usuario.email
    })