<script setup>
import { ref, watch, computed} from 'vue'
import usuarioDef from '@/assets/usuarioH.png'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/authService'
import BarraBusqueda from './BarraBusqueda.vue'

const moneda = ref([
{ title: 'Colombia COP $'},
{ title: 'Dolar $'}
])

const isOpen6 = ref(false) 

const menu = ref(false)

const router = useRouter()

const userStore = useAuthStore()

const usuarioLog = ref(true); 

const email = computed(() => userStore.email);

const irALogin = () => {
  router.push('/LoginUser')
}
const irARegister = () => {
  router.push('/RegisterUser')
}

const volverAMenu = () => {
  router.push('/')
}

watch(email, async () => {
  if (email.value != null ) {
    usuarioLog.value = ref(false)
  }
});

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
   
      <BarraBusqueda/>

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

      <v-card min-width="300" max-width="350">
        <v-list>
          <v-list-item
            :prepend-avatar="usuarioDef"
            :subtitle= userStore.email
            :title= userStore.usuario
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
          <v-list-item v-if="usuarioLog">
           <v-btn
            @click="irALogin"
            color="purple"
            block
            rounded="xl"
            class="text-white text-uppercase font-weight-bold">
            Iniciar Sesion
          </v-btn>
          </v-list-item>

          <v-list-item v-else>
           <v-btn
            @click="irALogin"
            color="purple"
            block
            rounded="xl"
            class="text-white text-uppercase font-weight-bold">
            Cerrar Sesion
          </v-btn>
          </v-list-item>

          <v-list-item v-if="usuarioLog">
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