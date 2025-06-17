import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/MenuPrincipal/HomeView.vue'  // Asegúrate de que existe

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'home', component: HomeView },  // Ruta principal
    { path: '/InventarioView', name: 'inventarioView', component: () => import('../views/VistaInventario/InventarioView.vue') },
    { path: '/DetalleProducto/:id', name: 'detalleProducto', component: () => import('../views/DetalleProducto/DetalleProducto.vue'), props: true },
    { path: '/ProductoCard', name: 'productoCard', component: () => import('../components/ProductoCard.vue') },
    { path: '/SalesForm', name: 'salesform', component: () => import('../views/RegistroPedido/SalesForm.vue') },
    { path: '/LoginUser', name: 'loginUser', component: () => import('../views/LoginUser/LoginUser.vue') },
    { path: '/RegisterUser', name: 'registerUser', component: () => import('../views/RegistroUser/RegisterUser.vue') },
  ],
})

export default router