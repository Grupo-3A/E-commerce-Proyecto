<template>
  <v-container fluid class="container">
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="6" lg="4">
        <v-card elevation="2" class="pa-4">
          <v-card-title class="justify-center">
            <span class="text-h5" style="color: var(--v-primary-base)">Crear Cuenta</span>
          </v-card-title>

          <v-form ref="form" @submit.prevent="handleRegister" v-model="valid">
            <v-text-field
              v-model="usuario.nombreUsu"
              label="Nombre de usuario"
              :rules="[v => !!v || 'Requerido']"
              outlined
              dense
              color="primary"
            />

            <v-text-field
              v-model="usuario.email"
              label="Correo electrónico"
              :rules="[v => /.+@.+\..+/.test(v) || 'Email inválido']"
              outlined
              dense
              color="primary"
            />

            <v-text-field
              v-model="usuario.password"
              label="Contraseña"
              :type="showPassword ? 'text' : 'password'"
              :append-icon="showPassword ? 'mdi-eye-off' : 'mdi-eye'"
              @click:append="showPassword = !showPassword"
              :rules="[v => v.length >= 6 || 'Mínimo 6 caracteres']"
              outlined
              dense
              color="primary"
            />

            <v-text-field
              v-model="usuario.telefono"
              label="Teléfono"
              outlined
              dense
              color="primary"
            />

            <v-text-field
              v-model="usuario.cedula"
              label="Cédula"
              outlined
              dense
              color="primary"
            />

            <v-text-field
              v-model="usuario.direccion"
              label="Dirección"
              outlined
              dense
              color="primary"
            />

            <v-textarea
              v-model="usuario.detDireccion"
              label="Detalle de dirección"
              rows="3"
              outlined
              dense
              color="primary"
            />

            <v-btn
              type="submit"
              :disabled="!valid"
              color="primary"
              class="mt-4"
              block
            >
              Registrar
            </v-btn>
          </v-form>

          <v-alert
            v-if="mensaje"
            type="success"
            class="mt-4"
            dismissible
            @dismissed="mensaje = ''"
          >
            {{ mensaje }}
          </v-alert>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref } from 'vue'
import { register } from '@/stores/authService'

const usuario = ref({
  nombreUsu: '', email: '', password: '', telefono: '', cedula: '', direccion: '', detDireccion: ''
})
const valid = ref(false)
const showPassword = ref(false)
const mensaje = ref('')
const form = ref(null)

const handleRegister = async () => {
  if (form.value.validate()) {
    try {
      await register(usuario.value)
      mensaje.value = 'Usuario registrado con éxito'
      form.value.resetValidation()
    } catch (err) {
      console.error('Error al registrar usuario:', err)
      mensaje.value = 'Error al registrar'
    }
  }
}
</script>

<style scoped>
/* Contenedor centrado y fondo */
.container {
  margin-top: 80px;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #ffffff;
  padding: 16px;
}

/* Tarjeta del formulario */
.card {
  background-color: rgba(255, 255, 255, 0.9);
  padding: 24px;
  border-radius: 16px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 400px;
}

/* Título */
.title {
  font-size: 24px;
  font-weight: bold;
  color: #5f259f; /* púrpura oscuro */
  text-align: center;
  margin-bottom: 16px;
}

/* Formulario y campos */
.form {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.input,
.textarea {
  width: 100%;
  padding: 8px 12px;
  border: 1px solid #7fa8d1; /* azul suave */
  border-radius: 8px;
  font-size: 14px;
  outline: none;
  transition: border-color 0.2s;
}

.input:focus,
.textarea:focus {
  border-color: #855cad; /* púrpura */
}

/* Botón */
.button {
  background-color: #855cad; /* púrpura */
  color: #ffffff;
  font-weight: 600;
  padding: 10px;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.2s;
}

.button:hover {
  background-color: #6e48a1;
}

/* Mensajes de error */
.error-message {
  margin-top: 4px;
  font-size: 12px;
  color: #d9534f;
  display: block;
}
</style>
