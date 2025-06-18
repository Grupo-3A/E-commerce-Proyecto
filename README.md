Aplicación Web Tienda de Motos

Este repositorio contiene una aplicación web full-stack para la venta de productos y accesorios para motocicletas. El proyecto incluye autenticación de usuarios, navegación y búsqueda de productos, funcionalidad de carrito de compras y un flujo de creación de pedidos.


Funcionalidades

Autenticación de usuarios: Registro e inicio de sesión con JWT.

Catálogo de productos: Inventario dinámico con categorías y páginas de detalle de producto.

Búsqueda: Buscar productos por nombre, categoría o marca.

Carrito de compras: Agregar, eliminar y actualizar cantidades de productos. El estado del carrito se persiste en localStorage y se sincroniza con la sesión del usuario.

Creación de pedidos: Proceso de checkout por pasos (stepper) para crear y enviar pedidos.

Diseño responsivo: Layout mobile-first usando Vuetify y CSS Grid.



Tecnologías utilizadasFrontend

Vue.js 3

Vuetify 3

Pinia (gestión de estado)

Vue Router

Axios (cliente HTTP)

CSS Grid & Flexbox

Backend

Flask (Python)

SQLAlchemy (ORM)

PostgreSQL (Base de datos)

JWT para autenticación

Herramientas de desarrollo

Node.js & npm

Python & pip

Git & GitHub

PyCharm / Visual Studio Code


Instalación y configuración

Backend

Clonar el repositorio

git clone https://github.com/tuusuario/motorcycle-store.git
cd motorcycle-store/backend

Crear y activar un entorno virtual

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Configurar variables de entorno. Crear un archivo .env con:

FLASK_APP=app.py
FLASK_ENV=development
DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/motorcycle_db
JWT_SECRET_KEY=tu_secreto_jwt

Ejecutar migraciones de base de datos

flask db upgrade

Iniciar el servidor Flask

flask runFrontend

Entrar al directorio del frontend

cd ../frontend

Instalar dependencias

npm install

Ejecutar servidor de desarrollo

npm run dev

Abrir en el navegador Visitar http://localhost:3000 (o el puerto que indique la consola).


Uso

Regístrate o inicia sesión con tus credenciales.

Navega por los productos en la página de inventario.

Busca productos mediante la barra de búsqueda o filtros de categoría.

Agrega productos al carrito.

Continúa al checkout, completa el formulario por pasos y envía tu pedido.

Contribuciones¡Las contribuciones son bienvenidas! Sigue estos pasos:
Realiza un fork del repositorio.
Crea una rama nueva: git checkout -b feature/MiNuevaFuncionalidad
Realiza tus cambios y haz commit: git commit -m 'Añade una nueva funcionalidad'
Sube tu rama: git push origin feature/MiNuevaFuncionalidad
Abre un Pull Request.
📄 LicenciaEste proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.
