<script setup>
import { computed, watch } from 'vue'
import { useCartStore } from '@/stores/carrito'
import { useRouter } from 'vue-router'
import axios from 'axios'

const props = defineProps(['modelValue'])
const emit = defineEmits(['update:modelValue'])

const cart = useCartStore()
const router = useRouter()

const cartTotal = computed(() => cart.cartTotal)

const drawerModel = computed({
  get: () => props.modelValue,
  set: (val) => emit('update:modelValue', val)
})

const closeDrawer = () => emit('update:modelValue', false)

const irASales = () => {
  router.push('/SalesForm')
}

const cargarCarrito = () => {
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
}

watch(drawerModel, (nuevoValor) => {
  if (nuevoValor === true) {
    cargarCarrito()
  }
})
</script>

<template>
  <v-navigation-drawer
    v-model="drawerModel"
    location="right"
    temporary
    width="500"
    class="bg-indigo-lighten-5 text-white"
  >
    <v-slide-y-transition>
      <v-toolbar flat class="bg-blue-grey-darken-4 text-white">
        <v-toolbar-title>Carrito de Compras</v-toolbar-title>
        <v-spacer />
        <v-btn icon @click="closeDrawer" color="white">
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </v-toolbar>
    </v-slide-y-transition>

    <v-divider class="border-opacity-1 bg-purple-darken-2"></v-divider>

    <v-list class="pa-4">
      <transition-group>
        <v-card
          v-for="(item, index) in cart.items"
          :key="index"
          class="mb-4 pa-3"
          elevation="6"
          rounded="lg"
          color="indigo-darken-4"
        >
          <v-row no-gutters align="center">
            <v-col cols="4">
              <v-img
                :src="item.image"
                width="80"
                height="80"
                cover
                class="rounded-lg elevation-2"
              />
            </v-col>
            <v-col cols="8" class="pl-4">
              <div class="text-h6 font-weight-bold text-blue-lighten-3">
                {{ item.name }}
              </div>
              <div class="text-body-2 text-white">Cantidad: {{ item.quantity }}</div>
              <div class="text-subtitle-2 font-weight-bold text-pink-accent-3">
                Precio: ${{ item.price }}
              </div>
            </v-col>
          </v-row>
        </v-card>
      </transition-group>
    </v-list>

    <v-divider class="my-2 border-opacity-25"></v-divider>

    <v-card flat class="pa-4 bg-purple-darken-2">
      <div class="text-subtitle-1 font-weight-bold mb-3 text-white">
        Total: ${{ cartTotal }}
      </div>
      <v-btn
        @click="irASales"
        color="deep-purple-lighten-3"
        block
        class="text-white text-uppercase font-weight-bold"
      >
        Ir al checkout
      </v-btn>
    </v-card>
  </v-navigation-drawer>
</template>