<script setup>
import { computed} from 'vue';

const props = defineProps(['modelValue'])
const emit = defineEmits(['update:modelValue'])

const drawerModelMenu = computed({
  get: () => props.modelValue,
  set: (val) => emit('update:modelValue', val)
})

const closeDrawer = () => emit('update:modelValue', false)

</script>

<template>
  <v-navigation-drawer
    v-model="drawerModelMenu"
    class="bg-deep-purple"
    theme="dark"
    location="start"
    temporary
    app
    width="350"
  >
    <v-slide-y-transition>
      <v-toolbar flat class="bg-blue-grey-darken-4 text-white">
        <v-toolbar-title>Menú Principal</v-toolbar-title>
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
      <v-list-item prepend-icon="mdi-view-dashboard" title="Dashboard" value="dashboard" />
      <v-list-item prepend-icon="mdi-forum" title="Mensajes" value="messages" />
    </v-list>
  </v-navigation-drawer>
</template>