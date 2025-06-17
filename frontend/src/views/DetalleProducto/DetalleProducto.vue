<template>
  <v-container fluid class="detalle-producto py-8">
    <div class="wrapper mx-auto">
      <v-card elevation="4" class="pa-8 white">
        <v-row align="start" justify="space-between">
          <!-- Imagen del producto -->
          <v-col cols="12" md="6">
            <v-img
              :src="producto.imagenPrin"
              alt="Imagen del producto"
              aspect-ratio="1"
              class="elevation-2 rounded-lg"
            />
          </v-col>

          <!-- Detalles e información -->
          <v-col cols="12" md="6" class="d-flex flex-column">
            <v-card-title class="titulo-producto mb-2 bg-indigo-lighten-5 pa-4 rounded">
              {{ producto.nombre }}
            </v-card-title>
            <v-card-subtitle class="precio-texto mb-6">
              ${{ new Intl.NumberFormat('es-CO').format(producto.precio) }}
            </v-card-subtitle>

            <!-- Detalles técnicos distribuidos -->
            <v-list dense class="info-adicional mb-6 bg-purple-darken-2 pa-4 rounded">
              <v-row>
                <v-col cols="6">
                  <span class="white--text"><strong>Marca:</strong> {{ producto.marca }}</span>
                </v-col>
                <v-col cols="6">
                  <span class="white--text"><strong>Categoría:</strong> {{ producto.categoria }}</span>
                </v-col>
                <v-col cols="6" class="mt-2">
                  <span class="white--text"><strong>Talla:</strong> {{ producto.talla }}</span>
                </v-col>
                <v-col cols="6" class="mt-2">
                  <span class="white--text"><strong>Stock:</strong> {{ producto.stock }}</span>
                </v-col>
              </v-row>
            </v-list>

            <!-- Descripción detallada -->
            <v-card-text class="descripcion mb-8">
              {{ producto.descripcion }}
            </v-card-text>

            <!-- Controles Favorito y Cantidad -->
            <v-row align="center" class="mb-6">
              <v-col cols="auto" class="d-flex align-center">
                <v-btn icon class="btn-favorito mr-3 elevation-2">
                  <v-icon size="28" color="red">mdi-heart-outline</v-icon>
                </v-btn>
                <span class="font-weight-medium purple--text text--darken-2">Favorito</span>
              </v-col>
              <v-col cols="auto" class="d-flex align-center">
                <span class="mr-2 font-weight-medium">Cantidad</span>
                <v-number-input
                  v-model.number="cantidad"
                  :min="1"
                  :max="producto.stock"
                  control-variant="split"
                  density="compact"
                  class="pa-0"
                  style="min-width: 4rem"
                  required
                />
              </v-col>
            </v-row>

            <!-- Botón Agregar al Carrito -->
            <v-btn
              class="btn-carrito"
              large
              rounded
              block
              @click="agregarAlCarrito"
            >
              <v-icon left>mdi-cart-plus</v-icon>
              Agregar al carrito
            </v-btn>
          </v-col>
        </v-row>
      </v-card>
    </div>
  </v-container>
</template>

<script setup>
import { computed, onMounted, ref, watch } from 'vue';
import { useRoute } from 'vue-router';
import { useProductoStore } from '@/stores/productos';
import { useCartStore } from '@/stores/carritoItems';

const route = useRoute();
const productoStore = useProductoStore();
const carrito = useCartStore();
const cantidad = ref(1);

const producto = computed(() => productoStore.productoActual);

onMounted(() => {
  productoStore.cargarProducto(route.params.id);
});

watch(
  () => route.params.id,
  (newId) => {
    productoStore.cargarProducto(newId);
  }
);

const agregarAlCarrito = () => {
  carrito.agregarItem({ ...producto.value, cantidad: cantidad.value });
};
</script>

<style scoped>
.detalle-producto {
  background-color: var(--v-deep-purple-lighten-3);
  width: 100vw;
  min-height: 100vh;

  justify-content: center;
  align-items: center;
  margin-top: 50px;
}

.wrapper {
  max-width: 1400px;
  padding: 0 2rem;
}

.titulo-producto {
  font-size: 2.5rem;
  font-weight: 700;
  color: var(--v-indigo-darken-2);
}

.precio-texto {
  font-size: 2rem;
  font-weight: 700;
  color: var(--v-purple-darken-2);
}

.descripcion {
  color: #333;
  line-height: 1.6;
}

.btn-favorito {
  background-color: white;
  color: var(--v-purple-darken-2);
  transition: background-color 0.3s;
}

.btn-favorito:hover {
  background-color: var(--v-purple-darken-2) !important;
  color: white;
}

.btn-carrito {
  background-color: var(--v-indigo-darken-2) !important;
  transition: background-color 0.3s;
}

.btn-carrito:hover {
  background-color: var(--v-purple-darken-2) !important;
}
</style>