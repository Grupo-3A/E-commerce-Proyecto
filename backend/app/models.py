from enum import unique
from app import db

class Productos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(300), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    imagen = db.Column(db.String(150))

    ItemCarros = db.relationship("ItemCarro", back_populates="producto", cascade="all, delete-orphan")


class CarroCompras(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subtotal = db.Column(db.Float, nullable=False)

    Pedido = db.relationship("Pedido", back_populates="CarroCompras", uselist=False)
    ItemCarros = db.relationship("ItemCarro", back_populates="carro", cascade="all, delete-orphan")


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