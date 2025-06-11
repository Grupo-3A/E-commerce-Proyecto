from enum import unique
from werkzeug.security import check_password_hash, generate_password_hash

from app import db

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String(100), nullable=False)

    producto = db.relationship("Productos", back_populates="Categoria")


class Marca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(100), nullable=False)

    producto = db.relationship("Productos", back_populates="Marca")


class Talla(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    talla = db.Column(db.String(100), nullable=False)

    producto = db.relationship("Productos", back_populates="Talla")


class Productos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(300), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    imagenPrin = db.Column(db.String(150))
    imagenesDet = db.Column(db.String(150))
    idCategoria = db.Column(db.Integer, db.ForeignKey("categoria.id"),nullable=True)
    idMarca = db.Column(db.Integer, db.ForeignKey("marca.id"), nullable=True)
    idTalla = db.Column(db.Integer, db.ForeignKey("talla.id"), nullable=True)

    ItemCarros = db.relationship("ItemCarro", back_populates="producto", cascade="all, delete-orphan")
    Favoritos = db.relationship("Favoritos", back_populates="producto", uselist=False)
    Categoria = db.relationship("Categoria", back_populates="producto")
    Marca = db.relationship("Marca", back_populates="producto")
    Talla = db.relationship("Talla", back_populates="producto")


class CarroCompras(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subtotal = db.Column(db.Float, nullable=False)
    idUsuario = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=True)

    Pedido = db.relationship("Pedido", back_populates="CarroCompras", uselist=False)
    ItemCarros = db.relationship("ItemCarro", back_populates="carro", cascade="all, delete-orphan")
    Usuarios = db.relationship("Usuarios", back_populates="CarroCompras", uselist=False)


class ItemCarro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idProductos = db.Column(db.Integer, db.ForeignKey("productos.id"), nullable=False)
    idCarro = db.Column(db.Integer, db.ForeignKey("carro_compras.id"), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)

    producto = db.relationship("Productos", back_populates="ItemCarros")
    carro = db.relationship("CarroCompras", back_populates="ItemCarros")


class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombreUsuario = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(10), nullable=False)
    direccion = db.Column(db.String(200), nullable=False)
    detalleDireccion = db.Column(db.String(200), nullable=False)
    cedula = db.Column(db.String(10), nullable=False)
    idCarroCom = db.Column(db.Integer, db.ForeignKey("carro_compras.id"), unique=True, nullable=False)

    CarroCompras = db.relationship("CarroCompras", back_populates="Pedido", uselist=False)


class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombreUsu = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(10), nullable=False)
    direccion = db.Column(db.String(200), nullable=False)
    detDireccion = db.Column(db.String(200), nullable=False)
    cedula = db.Column(db.String(10), nullable=False)

    CarroCompras = db.relationship("CarroCompras", back_populates="Usuarios", uselist=False)
    Favoritos = db.relationship("Favoritos", back_populates="usuario", uselist=False)

    def set_password(self, contraseña):
        self.password = generate_password_hash(contraseña)

    def check_password(self, contraseña):
        return check_password_hash(self.password, contraseña)


class Favoritos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idProductos = db.Column(db.Integer, db.ForeignKey("productos.id"), nullable=False)
    idUsuario = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)

    producto = db.relationship("Productos", back_populates="Favoritos")
    usuario = db.relationship("Usuarios", back_populates="Favoritos")






