<script setup>
import { ref } from 'vue'
import NavBar from '@/components/NavBar.vue'
import SubNavBar from './components/SubNavBar.vue'
import NavigationMenu from '@/components/Navigation-Menu.vue'
import NavigationDrawer from '@/components/Navigation-Drawer.vue'

const isMenuOpen = ref(false)
const isCartOpen = ref(false)
</script>

<template>
  <v-app>
    <NavBar 
      @toggle-cart="isCartOpen = !isCartOpen"
    />
    <SubNavBar
    @toggle-menu="isMenuOpen = !isMenuOpen" 
    />
    <NavigationMenu v-model="isMenuOpen" />
>
    <NavigationDrawer v-model="isCartOpen" />

    <v-main style="--v-layout-top: 0px;">
      <router-view />
    </v-main>
  </v-app>
</template>


