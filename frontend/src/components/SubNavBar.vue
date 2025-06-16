<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useProductoStore } from '@/stores/Productos';

const router = useRouter()
const inventario = useProductoStore();

const indumentariaTop = ref([
{ title: 'Chaquetas', value: 2 },
{ title: 'Pantalones', value: 17},
{ title: 'Botas', value: 4},
{ title: 'Rodilleras', value: 5},
{ title: 'Guantes', value: 3}
])

const cascos = ref([
{ title: 'LS2', value: 3},
{ title: 'AGV', value: 1},
{ title: 'SHAFT', value: 2}
])

const repuestos = ref([
{ title: 'SUSUKI', value: 5},
{ title: 'YAMAHA', value: 6},
{ title: 'BAJAJ', value: 7},
{ title: 'DUCATI', value: 8},
{ title: 'AUTECO', value: 9},
{ title: 'KTM', value: 10}
])

const accesorios = ref([
{ title: 'Defensas', value: 6},
{ title: 'Soportes', value: 8},
{ title: 'Bases', value: 9},
{ title: 'Intercomunicadores', value: 10}
])


const isOpen1 = ref(false) 
const isOpen2 = ref(false) 
const isOpen3 = ref(false) 
const isOpen4 = ref(false) 

const irAProductos = () => {
  router.push('/InventarioView')
  inventario.cargarProductos()
}
const irAProductosMarca = (idMarca) => {
  router.push('/InventarioView')
  inventario.cargarProductosPorMarca(idMarca)
}
const irAProductosCategoria = (idCategoria) => {
  router.push('/InventarioView')
  inventario.cargarProductosPorCategoria(idCategoria)
}
</script>

<template>
  <v-app-bar color="teal-darken-4">
        <template v-slot:image>
          <v-img
            gradient="to top right, rgba(0, 3, 3, 0.8), rgba(57, 65, 64, 0.8)"
          ></v-img>
        </template>

    
        <template v-slot:prepend>
          <v-app-bar-nav-icon
            color="rgba(12, 223, 223, 0.96)"
            @click="$emit('toggle-menu')"
          />
        </template>
    
        
        <v-spacer></v-spacer>  

        <v-menu v-model="isOpen1">
        <template v-slot:activator="{ props }">
          <v-btn v-bind="props" variant="text">
            Indumentaria Top
          <v-icon color="rgba(12, 223, 223, 0.96)">{{ isOpen1 ? 'mdi-menu-up' : 'mdi-menu-down' }}</v-icon>
          </v-btn>
        </template>

        <v-list>
          <v-list-item
            v-for="(item, index) in indumentariaTop"
            :key="index"
          >
            <v-list-item-title @click="irAProductosCategoria(item.value)" >{{ item.title }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>


      <v-menu v-model="isOpen2">
        <template v-slot:activator="{ props }">
          <v-btn v-bind="props" variant="text">
            Cascos
          <v-icon color="rgba(12, 223, 223, 0.96)">{{ isOpen2 ? 'mdi-menu-up' : 'mdi-menu-down' }}</v-icon>
          </v-btn>
        </template>

        <v-list>
          <v-list-item
            v-for="(item, index) in cascos"
            :key="index"
          >
            <v-list-item-title @click="irAProductosMarca(item.value)">{{ item.title }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>

      <v-menu v-model="isOpen3">
        <template v-slot:activator="{ props }">
          <v-btn v-bind="props" variant="text">
            Repuestos
          <v-icon color="rgba(12, 223, 223, 0.96)">{{ isOpen3 ? 'mdi-menu-up' : 'mdi-menu-down' }}</v-icon>
          </v-btn>
        </template>

        <v-list>
          <v-list-item
            v-for="(item, index) in repuestos"
            :key="index"

          >
            <v-list-item-title @click="irAProductosMarca(item.value)">{{ item.title }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>

      <v-menu v-model="isOpen4">
        <template v-slot:activator="{ props }">
          <v-btn v-bind="props" variant="text">
            Accesorios para Motos
          <v-icon color="rgba(12, 223, 223, 0.96)">{{ isOpen4 ? 'mdi-menu-up' : 'mdi-menu-down' }}</v-icon>
          </v-btn>
        </template>

        <v-list>
          <v-list-item
            v-for="(item, index) in accesorios"
            :key="index"
          >
            <v-list-item-title @click="irAProductosCategoria(item.value)">{{ item.title }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>


      <v-spacer></v-spacer>  

        <v-btn icon color="rgba(12, 223, 223, 0.96)">
          <v-icon @click="irAProductos" >mdi-magnify</v-icon>
        </v-btn>

        <v-btn icon color="rgba(12, 223, 223, 0.96)">
          <v-icon>mdi-headset</v-icon>
        </v-btn>
      </v-app-bar>
   </template>