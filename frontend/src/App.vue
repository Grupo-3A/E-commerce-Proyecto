<script setup>
import NavBar from '@/components/NavBar.vue'
import axios from 'axios'
import { useCartStore } from '@/stores/carrito'
import { onMounted } from 'vue'

const cart = useCartStore()


onMounted(() => {
  axios.get('http://127.0.0.1:5000/item_carro/por-carro/2')
    .then(res => {
      const items = res.data.map(item => ({
        name: item.nombre,
        quantity: item.cantidad,
        price: item.precio,
        image: item.imagen
      }))
      cart.setItems(items)
    })
    .catch(err => {
      console.error('Error al cargar carrito:', err)
    })
})
</script>

<template>
  <NavBar  />
  <router-view />
</template>


  