<template>
  <div v-if="producto">
    <h1>{{ producto.nombre }}</h1>
    <img :src="producto.imagenPrin" alt="Imagen del producto" class="w-64 h-64" />
    <p>{{ producto.descripcion }}</p>
    <p>Marca: {{ producto.marca }}</p>
    <p>Categoría: {{ producto.categoria }}</p>
    <p>Precio: ${{ producto.precio }}</p>
    <p>Talla: {{ producto.talla }}</p>
    <p>Stock: {{ producto.stock }}</p>

    <button @click="agregarAlCarrito">Agregar al carrito</button>
  </div>
  <div v-else>
    <p>Cargando producto...</p>
  </div>
</template>

<script setup>
import { computed, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { useProductoStore } from '@/stores/Productos';
import { useCartStore } from '@/stores/carritoItems';

const route = useRoute();
const productoStore = useProductoStore();
const carrito = useCartStore();

// Enlazamos directamente al objeto del store
const producto = computed(() => productoStore.productoActual);

onMounted(() => {
  productoStore.cargarProducto(route.params.id);
});

const agregarAlCarrito = () => {
  carrito.agregarItem(producto.value);
};
</script>