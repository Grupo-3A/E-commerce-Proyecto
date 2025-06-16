<script setup>
import { ref} from 'vue'
import usuarioDef from '@/assets/usuarioDef.png'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/authService'
import debounce from 'lodash/debounce'
import { useProductoStore } from '@/stores/Productos'

const moneda = ref([
{ title: 'Colombia COP $'},
{ title: 'Dolar $'}
])

const isOpen6 = ref(false) 

const menu = ref(false)

const productoStore = useProductoStore()

const router = useRouter()

const usuarioLog = useAuthStore()

const irALogin = () => {
  router.push('/LoginUser')
}
const irARegister = () => {
  router.push('/RegisterUser')
}

const volverAMenu = () => {
  router.push('/')
}


// Estado
const searchQuery = ref('')
const liveResults = ref([])
const menuOpen    = ref(false)

// 1) fetchLive lee siempre de searchQuery.value
const fetchLive = debounce(async () => {
  const q = String(searchQuery.value || '').trim()
  if (!q) {
    liveResults.value = []
    menuOpen.value = false
    return
  }
  liveResults.value = await productoStore.cargarProductos(q)
  menuOpen.value = liveResults.value.length > 0
}, 1000)

// 2) onInput dispara fetchLive sin argumentos
function onInput() {
  fetchLive()
}

// 3) onSelect con objeto producto
function onSelect(prod) {
  menuOpen.value = false
  searchQuery.value = ''
  router.push({ name: 'detalleProducto', params: { id: prod.id }})
}

// 4) onEnter para ir a inventario
function onEnter() {
  const q = String(searchQuery.value || '').trim()
  if (!q) return
  menuOpen.value = false
  router.push('/InventarioView')
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
        <v-btn icon color="rgba(12, 223, 223, 0.96)">
            <v-icon @click="volverAMenu">mdi-home</v-icon>
        </v-btn>
      </template>

      <v-spacer/>
   
      <!-- Buscador -->
    <div style="position: relative; flex: 1; max-width: 400px; margin: 0 16px;">
      <v-text-field
        v-model="searchQuery"
        placeholder="Buscar productos..."
        append-inner-icon="mdi-magnify"
        dense flat hide-details
        @input="onInput"
        @keyup.enter="onEnter"
        @click:append-inner="onEnter"
      />

      <!-- Menú de sugerencias básico -->
      <v-menu
        v-model="menuOpen"
        activator="parent"
        offset-y
        max-width="400"
      >
        <v-list>
          <v-list-item
            v-for="p in liveResults"
            :key="p.id"
            @click="onSelect(p)"
            ripple
          >
            <v-list-item-title>{{ p.nombre }} — ${{ p.precio }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </div>


    <v-spacer/>

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

      <!--boton usuario iniciar y registrarse-->
  <div class="text-center">
    <v-menu
      v-model="menu"
      :close-on-content-click="false"
    >
      <template v-slot:activator="{ props }">
        <v-btn
          color="rgba(190, 24, 60, 0.96)"
          v-bind="props"
        >
          <v-icon size="26">mdi-account</v-icon>
        </v-btn>
      </template>

      <v-card min-width="300">
        <v-list>
          <v-list-item
            :prepend-avatar="usuarioDef"
            :subtitle= usuarioLog.email
            :title= usuarioLog.usuario
          >
            <template v-slot:append>
              <v-btn
                :class=" 'text-grey'"
                icon="mdi-account"
                variant="text"
                
              ></v-btn>
            </template>
          </v-list-item>
        </v-list>

        <v-divider></v-divider>

        <v-list>
          <v-list-item>
           <v-btn
            @click="irALogin"
            color="purple"
            block
            rounded="xl"
            class="text-white text-uppercase font-weight-bold">
            Iniciar Sesion
          </v-btn>
          </v-list-item>

          <v-list-item >
          <v-btn
            @click="irARegister"
            color="purple"
            block
            rounded="xl"
            class="text-white text-uppercase font-weight-bold">
            Registrarse
          </v-btn>
             
          </v-list-item>
        </v-list>
      </v-card>
    </v-menu>
  </div>

        
        <v-btn 
            icon 
            color="rgba(190, 24, 60, 0.96)" 
            @click="$emit('toggle-cart')"
          >
            <v-icon>mdi-cart</v-icon>
          </v-btn>
        </v-app-bar>
        
   </template>