<template>
  <v-card class="flex-1 flex flex-col">
    <template v-slot:loader="{ isActive }">
      <v-progress-linear
        :active="isActive"
        color="deep-purple"
        height="4"
        indeterminate
      ></v-progress-linear>
    </template>

    <v-img
      height="250"
      :src="producto.imagenPrin"
      cover
    ></v-img>

    <v-card-item>
      <v-card-title class="truncate">{{ producto.nombre }}</v-card-title>
      <v-card-subtitle>
        <span>{{ producto.marca }}</span>
        <v-icon color="error" icon="mdi-fire-circle" size="small"></v-icon>
      </v-card-subtitle>
    </v-card-item>

    <v-card-text>
  <v-row 
    align="center" 
    justify="space-between"
    class="px-4"
  >
    <v-col cols="auto" class="d-flex align-center">
      <v-rating
        :model-value="4.5"
        color="amber"
        density="compact"
        size="small"
        half-increments
        readonly
      />
      <span class="text-grey ms-2">4.5 (413)</span>
    </v-col>

    <v-col cols="auto">
      <div class="text-h6 font-weight-bold">${{ producto.precio }}</div>
    </v-col>
  </v-row>

  <div class="px-4 mt-2 text-body-2 truncate">
    {{ producto.descripcion }}
  </div>
</v-card-text>



    <v-divider class="mx-4 mb-1"></v-divider>

    <v-card-title>Tallas Disponibles</v-card-title>
    <div class="px-4 mb-2">
      <v-chip-group selected-class="bg-deep-purple-lighten-2">
        <v-chip>{{ producto.talla }}</v-chip>
      </v-chip-group>
    </div>

    <v-card-actions class="mt-auto d-flex align-center justify-space-between">
      <!-- Bloque cantidad -->
      <div class="d-flex align-center">
        <span class="mr-2 font-weight-medium">Cantidad</span>
        <v-number-input
          :max="20"
          :min="1"
          control-variant="split"
          density="compact"
          class="pa-0"
          style="min-width: 2rem;"
          required
          v-model.number="cantidad"
        />
      </div>
    </v-card-actions>

    <v-card-actions class="mt-auto">
      <v-btn
        color="deep-purple-lighten-2"
        text="Ver Más"
        border
        @click="verDetalle"
      ></v-btn>
      <v-btn
        color="deep-purple-lighten-2"
        text="Agregar"
        border
        @click="agregarAlCarrito"
      ></v-btn>
    </v-card-actions>
  </v-card>
</template>

<script setup>
import { useRouter } from 'vue-router';
import { useCartStore } from '@/stores/carritoItems';
import { carroCompraStore } from '@/stores/carroCompras';
import { useAuthStore } from '@/stores/authService';
import { ref } from 'vue';

const props = defineProps({ producto: Object });
const router = useRouter();
const itemCarro = useCartStore();
const carroCompras = carroCompraStore();
const auth = useAuthStore();

const cantidad = ref(null);

function verDetalle() {
  router.push({ name: 'detalleProducto', params: { id: props.producto.id } });
}
async function agregarAlCarrito() {
  const qty = Number(cantidad.value) 
  await itemCarro.addToCart(props.producto, carroCompras.id, qty);
  const nuevoSub = itemCarro.subtotal
  await carroCompras.actualizarCarroCompras(carroCompras.id, auth.id, nuevoSub) 
}
</script>

<style scoped>
.v-card {
  display: flex;
  flex-direction: column;
  height: 100%;
}

</style>