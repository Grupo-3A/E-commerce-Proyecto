<script setup>
import { computed } from 'vue';
import { useAuthStore } from '@/stores/authService'
import { useRouter } from 'vue-router'
import { useProductoStore } from '@/stores/productos';

const router = useRouter()
const inventario = useProductoStore();

const userAuth = useAuthStore()

const props = defineProps(['modelValue']);
const emit = defineEmits(['update:modelValue']);

const drawerModelMenu = computed({
  get: () => props.modelValue,
  set: (val) => emit('update:modelValue', val),
});

const closeDrawer = () => emit('update:modelValue', false);

const irAProductos = () => {
  router.push('/InventarioView')
  inventario.cargarProductos()
}

const irAFavoritos = () => {
  router.push('/InventarioView')
  inventario.cargarFavoritos(userAuth.id)
}
</script>

<template>
  <v-navigation-drawer
    v-model="drawerModelMenu"
    class="deep-purple-lighten-3 white--text elevation-2"
    temporary
    app
    width="264"
  >
    <!-- Toolbar con título y botón de cierre -->
    <v-slide-y-transition>
      <v-toolbar flat class="bg-purple-darken-2 white--text">
        <v-toolbar-title>Mi Tienda</v-toolbar-title>
        <v-spacer />
        <v-btn icon @click="closeDrawer" class="white--text">
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </v-toolbar>
    </v-slide-y-transition>

    <!-- Avatar de usuario opcional -->
    <v-list class="bg-indigo-lighten-5 pa-3 rounded-sm" >
      <v-list-item>
          <v-avatar size="80" >
          <img src="@/assets/usuarioH.png" alt="Avatar Usuario"  class="imagen-usuario"/>
        </v-avatar>
      
      
        <v-list-item-content class="texto-user">
          <v-list-item-title class="white--text texto-user">Bienvenido, {{ userAuth.usuario }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>

    <v-divider class="my-4"></v-divider>

    <!-- Menú principal -->
    <v-list dense nav>
      <v-list-item link @click="irAProductos" class="white--text rounded-sm mb-2">
        <v-list-item-icon><v-icon>mdi-package-variant-closed</v-icon></v-list-item-icon>
        <v-list-item-title>Todos los productos</v-list-item-title>
      </v-list-item>
      <v-list-item link @click="irAFavoritos" class="white--text rounded-sm mb-2">
        <v-list-item-icon><v-icon>mdi-heart</v-icon></v-list-item-icon>
        <v-list-item-title>Favoritos</v-list-item-title>
      </v-list-item>
      <v-list-item link @click="closeDrawer" class="white--text rounded-sm mb-2">
        <v-list-item-icon><v-icon>mdi-cart</v-icon></v-list-item-icon>
        <v-list-item-title>Mis pedidos</v-list-item-title>
      </v-list-item>
      <v-list-item link @click="closeDrawer" class="white--text rounded-sm mb-2">
        <v-list-item-icon><v-icon>mdi-account</v-icon></v-list-item-icon>
        <v-list-item-title>Mi cuenta</v-list-item-title>
      </v-list-item>
      <v-list-item link @click="closeDrawer" class="white--text rounded-sm mb-2">
        <v-list-item-icon><v-icon>mdi-cog</v-icon></v-list-item-icon>
        <v-list-item-title>Configuración</v-list-item-title>
      </v-list-item>
      <v-list-item link @click="closeDrawer" class="white--text rounded-sm mb-2">
        <v-list-item-icon><v-icon>mdi-help-circle</v-icon></v-list-item-icon>
        <v-list-item-title>Ayuda</v-list-item-title>
      </v-list-item>
      <v-list-item link @click="closeDrawer" class="white--text rounded-sm">
        <v-list-item-icon><v-icon>mdi-information</v-icon></v-list-item-icon>
        <v-list-item-title>Acerca de</v-list-item-title>
      </v-list-item>
    </v-list>

    <v-spacer></v-spacer>

    <!-- Cerrar sesión al final -->
    <v-list dense class="logout-item nav">
      <v-list-item link @click="closeDrawer" class="white--text rounded-sm">
        <v-list-item-icon><v-icon>mdi-logout</v-icon></v-list-item-icon>
        <v-list-item-title>Cerrar sesión</v-list-item-title>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<style scoped>
/* Hover con bg-purple-darken-2 */
.v-list-item:hover {
  background-color: var(--v-purple-darken-2) !important;
}

/* Ajuste de bordes redondeados para los items */
.rounded-sm {
  border-radius: 8px;
}

.imagen-usuario{
  max-width: 5vw;
}

.texto-user{
  margin-top: 15px;
}
</style>
