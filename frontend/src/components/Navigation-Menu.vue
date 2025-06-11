<script setup>
import { computed, watch } from 'vue';

const props = defineProps(['modelValue'])
const emit = defineEmits(['update:modelValue'])

const drawerModelMenu = computed({
  get: () => props.modelValue,
  set: (val) => emit('update:modelValue', val)
})

const closeDrawer = () => emit('update:modelValue', false)

watch (drawerModelMenu, (nuevoValor) => {
  if (nuevoValor === true) {
   console.log('Entra al watch')
  }
})
</script>

<template>
        <v-navigation-drawer
          v-model="drawerModelMenu"
          class="bg-deep-purple"
          theme="dark"
          app
          location="start"
          temporary
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
        <v-list>
          <v-list-item
            prepend-avatar="https://randomuser.me/api/portraits/women/75.jpg"
          ></v-list-item>
        </v-list>

        <v-divider></v-divider>

        <v-list density="compact" nav>
          <v-list-item
            prepend-icon="mdi-view-dashboard"
            value="dashboard"
          ></v-list-item>

          <v-list-item prepend-icon="mdi-forum" value="messages"></v-list-item>
        </v-list>
      </v-navigation-drawer>

      <v-navigation-drawer permanent>
        <v-list>
          <v-list-item title="Home" value="home"></v-list-item>

          <v-list-item title="Contacts" value="contacts"></v-list-item>

          <v-list-item title="Settings" value="settings"></v-list-item>
        </v-list>
      </v-navigation-drawer>

      <v-main style="height: 300px"></v-main>
</template>