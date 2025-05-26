<template>
    <div>
      <h2>Registro</h2>
      <form @submit.prevent="handleRegister">
        <input v-model="usuario.nombreUsu" placeholder="Nombre de usuario" required />
        <input v-model="usuario.email" type="email" placeholder="Correo" required />
        <input v-model="usuario.password" type="password" placeholder="Contraseña" required />
        <input v-model="usuario.telefono" placeholder="Teléfono" required />
        <input v-model="usuario.direccion" placeholder="Dirección" required />
        <input v-model="usuario.detDireccion" placeholder="Detalle Dirección" required />
        <input v-model="usuario.cedula" placeholder="Cédula" required />
        <button type="submit">Registrar</button>
      </form>
      <p v-if="mensaje">{{ mensaje }}</p>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { register } from '@/stores/authService';
  
  const usuario = ref({
    nombreUsu: '',
    email: '',
    password: '',
    telefono: '',
    direccion: '',
    detDireccion: '',
    cedula: ''
  });
  
  const mensaje = ref('');
  
  const handleRegister = async () => {
    try {
      await register(usuario.value);
      mensaje.value = 'Usuario registrado con éxito';
    } catch (err) {
      console.error('Error al registrar usuario:', err)
      mensaje.value = 'Error al registrar';
    }
  };
  </script>