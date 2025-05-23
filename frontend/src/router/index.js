import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'  // Asegúrate de que existe

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'home', component: HomeView },  // Ruta principal
    { path: '/ProductLs2', name: 'productls2', component: () => import('../views/ProductLs2.vue') },
    { path: '/ProductShaft', name: 'productshaft', component: () => import('../views/ProductShaft.vue') },
    { path: '/ProductAgv', name: 'productagv', component: () => import('../views/ProductAgv.vue') },
  ],
})

export default router