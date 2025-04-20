<script setup>
import { useRouter } from 'vue-router'
import { ref } from 'vue'
import { useCartStore } from '@/stores/carrito'
const cart = useCartStore()

const router = useRouter()

const irASales = () => {
  router.push('/SalesForm')
}

const indumentariaTop = ref([
{ title: 'Chaquetas', link: '/' },
{ title: 'Pantalones', link: '/productos' },
{ title: 'Botas', link: '/servicios' },
{ title: 'Rodilleras', link: '/contacto' },
{ title: 'Inpermeables', link: '/contacto' },
{ title: 'Guantes', link: '/contacto' }
])

const cascos = ref([
{ title: 'LS2', link: '/' },
{ title: 'AGV', link: '/productos' },
{ title: 'SHAFT', link: '/servicios' }
])

const repuestos = ref([
{ title: 'SUSUKI', link: '/' },
{ title: 'YAMAHA', link: '/productos' },
{ title: 'BAJAJ', link: '/servicios' },
{ title: 'DUCATI', link: '/servicios' },
{ title: 'AUTECO', link: '/servicios' },
{ title: 'KTM', link: '/servicios' }
])

const accesorios = ref([
{ title: 'Defensas', link: '/' },
{ title: 'Protectores', link: '/productos' },
{ title: 'Soportes', link: '/servicios' },
{ title: 'Bases', link: '/servicios' },
{ title: 'Intercomunicadores', link: '/servicios' }
])

const mantenimiento = ref([
{ title: 'Herramientas', link: '/' },
{ title: 'Lubricantes', link: '/productos' },
{ title: 'Filtros', link: '/servicios' },
{ title: 'Frenos', link: '/servicios' },
{ title: 'Quimicos', link: '/servicios' }
])

const moneda = ref([
{ title: 'Colombia COP $', link: '/' },
{ title: 'Dolar $', link: '/productos' }
])

const isOpen1 = ref(false) 
const isOpen2 = ref(false) 
const isOpen3 = ref(false) 
const isOpen4 = ref(false) 
const isOpen5 = ref(false) 
const isOpen6 = ref(false) 
const isCartOpen = ref(false)
</script>

<template>
    <v-layout>

      <v-app-bar color="teal-darken-4">
        <template v-slot:image>
          <v-img
            gradient="to top right, rgba(0, 3, 3, 0.8), rgba(57, 65, 64, 0.8)"
          ></v-img>
        </template>

        <template v-slot:prepend>
          <v-app-bar-nav-icon color="rgba(12, 223, 223, 0.96)"></v-app-bar-nav-icon>
        </template>

        <v-menu v-model="isOpen6">
        <template v-slot:activator="{ props }">
          <v-btn v-bind="props" variant="text" color="rgba(12, 223, 223, 0.96)">
              Colombia COP $
          <v-icon >{{ isOpen6 ? 'mdi-menu-up' : 'mdi-menu-down' }}</v-icon>
          </v-btn>
        </template>

        <v-list>
          <v-list-item
            v-for="(item, index) in moneda"
            :key="index"
            :to="item.link"
          >
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>

        <v-btn icon color="rgba(190, 24, 60, 0.96)">
          <v-icon>mdi-account</v-icon>
        </v-btn>
        
        <v-btn icon color="rgba(190, 24, 60, 0.96)" @click="isCartOpen = true">
          <v-icon>mdi-cart</v-icon>
        </v-btn>

      </v-app-bar>

      
          <v-navigation-drawer
          v-model="isCartOpen"
          location="right"
          temporary
          width="500"
        >
          <v-toolbar flat>
            <v-toolbar-title>Carrito de Compras</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn icon @click="isCartOpen = false">
              <v-icon>mdi-close</v-icon>
            </v-btn>
          </v-toolbar>

          <v-divider></v-divider>

          <v-list>
            <v-list-item
                v-for="(item, index) in cart.items"
                :key="index"
              >
                <v-row no-gutters>
                  <v-col cols="4">
                    <v-img
                      :src="item.image"
                      width="80"
                      height="80"
                      cover
                      class="rounded"
                    />
                  </v-col>
                  <v-col cols="8" class="pl-4">
                    <v-list-item-title>{{ item.name }}</v-list-item-title>
                    <v-list-item-subtitle>Cantidad: {{ item.quantity }}</v-list-item-subtitle>
                    <v-list-item-subtitle>Precio: ${{ item.price }}</v-list-item-subtitle>
                  </v-col>
                </v-row>
                <v-divider class="my-2"></v-divider>
              </v-list-item>
          </v-list>



          <v-card flat class="pa-4">
            <v-btn @click="irASales" color="primary" block>Ir al checkout</v-btn>
          </v-card>
        </v-navigation-drawer>
        
        


        
      <v-app-bar color="teal-darken-4">
        <template v-slot:image>
          <v-img
            gradient="to top right, rgba(0, 3, 3, 0.8), rgba(57, 65, 64, 0.8)"
          ></v-img>
        </template>

        <template v-slot:prepend>
          <v-app-bar-nav-icon color="rgba(12, 223, 223, 0.96)"></v-app-bar-nav-icon>
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
            :to="item.link"
          >
            <v-list-item-title>{{ item.title }}</v-list-item-title>
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
            :to="item.link"
          >
            <v-list-item-title>{{ item.title }}</v-list-item-title>
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
            :to="item.link"
          >
            <v-list-item-title>{{ item.title }}</v-list-item-title>
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
            :to="item.link"
          >
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>

      <v-menu v-model="isOpen5">
        <template v-slot:activator="{ props }">
          <v-btn v-bind="props" variant="text" >
            Mantenimiento y Cuidado
          <v-icon color="rgba(12, 223, 223, 0.96)"> {{ isOpen5 ? 'mdi-menu-up' : 'mdi-menu-down' }}</v-icon>
          </v-btn>
        </template>

        <v-list>
          <v-list-item
            v-for="(item, index) in mantenimiento"
            :key="index"
            :to="item.link"
          >
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>


      <v-spacer></v-spacer>  

        <v-btn icon color="rgba(12, 223, 223, 0.96)">
          <v-icon>mdi-magnify</v-icon>
        </v-btn>

        <v-btn icon color="rgba(12, 223, 223, 0.96)">
          <v-icon>mdi-dots-vertical</v-icon>
        </v-btn>
      </v-app-bar>

    </v-layout>
   </template>