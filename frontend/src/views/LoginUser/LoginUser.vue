<template>
  <v-container class="container" fluid>
    <v-row justify="center">
      <v-col cols="12" sm="8" md="6" lg="4">
        <v-card class="pa-6 rounded-xl elevation-8">
          <v-card-title class="text-h5 text-center">Iniciar sesión</v-card-title>

          <v-form @submit.prevent="handleLogin" class="mt-4" ref="form">
            <v-text-field
              v-model="email"
              label="Correo electrónico"
              type="email"
              prepend-icon="mdi-email"
              required
            ></v-text-field>

            <v-text-field
              v-model="password"
              label="Contraseña"
              type="password"
              prepend-icon="mdi-lock"
              required
            ></v-text-field>

            <v-btn
              type="submit"
              color="primary"
              block
              class="mt-4"
              :loading="loading"
            >
              Entrar
            </v-btn>
          </v-form>

          <v-alert
            v-if="error"
            type="error"
            variant="tonal"
            class="mt-4"
            dismissible
          >
            {{ error }}
          </v-alert>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref } from 'vue';
import { login } from '@/stores/authService';
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/authService';
import { carroCompraStore } from '@/stores/carroCompras';
import { useCartStore } from '@/stores/carritoItems';

const email = ref('');
const password = ref('');
const error = ref('');
const loading = ref(false);
const router = useRouter();

const carroStore = carroCompraStore();
const authStore = useAuthStore();
const cart = useCartStore();

const handleLogin = async () => {
  error.value = '';
  loading.value = true;
  try {
    const response = await login(email.value, password.value);
    const usuario = response.usuario;

    authStore.iniciarSesion(response.token, usuario.id, usuario.nombre, usuario.email);
    carroStore.actualizarCarroCompras(carroStore.id, usuario.id, cart.subtotal);

    router.push('/');
  } catch (err) {
    console.error('Error al iniciar sesión:', err);
    error.value = 'Credenciales inválidas';
  } finally {
    loading.value = false;
  }
};
</script>

<style scoped>
/* Contenedor centrado y fondo */
.container {
  width: 100vw;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #ffffff;
  padding: 16px;
}

</style>