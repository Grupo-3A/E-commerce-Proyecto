<script setup>
import { ref} from 'vue'
import { useRouter } from 'vue-router'
import debounce from 'lodash/debounce'
import { useProductoStore } from '@/stores/productos'

const productoStore = useProductoStore()

const router = useRouter()

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
      <div class="d-flex align-center" style="flex: 1; max-width: 600px; position: relative;">
      <v-hover v-slot="{ isHovering, props }">
        <v-text-field
          v-model="searchQuery"
          placeholder="Buscar productos..."
          variant="solo"
          density="compact"
          hide-details
          flat
          rounded
          prepend-inner-icon="mdi-magnify"
          v-bind="props"
          @input="onInput"
          @keyup.enter="onEnter"
          @click:append-inner="onEnter"
          :style="{
            width: '100%',
            boxShadow: isHovering ? '0 2px 8px rgba(0,0,0,0.2)' : 'none',
            transition: 'box-shadow 0.3s ease'
          }"
        />
      </v-hover>


      <v-menu
        v-model="menuOpen"
        activator="parent"
        offset-y
        max-width="600"
      >
        <v-sheet rounded="lg" elevation="4" class="pa-2">
          <v-list dense style="max-height: 300px; overflow-y: auto;">
            <template v-if="liveResults.length">
              <v-list-item
                v-for="p in liveResults"
                :key="p.id"
                @click="onSelect(p)"
                class="transition-colors"
                active-class="bg-grey-lighten-4"
                ripple
                rounded
              >
                <v-list-item-content>
                  <v-list-item-title class="font-medium">{{ p.nombre }}</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
  
            </template>
            <template v-else>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title class="text-center text--disabled">
                    No se encontraron productos
                  </v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </template>
          </v-list>
        </v-sheet>
      </v-menu>
    </div>
</template>