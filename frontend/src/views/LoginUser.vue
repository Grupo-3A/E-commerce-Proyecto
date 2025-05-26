<template>
    <div>
      <h2>Login</h2>
      <form @submit.prevent="handleLogin">
        <input v-model="email" type="email" placeholder="Correo" required />
        <input v-model="password" type="password" placeholder="Contraseña" required />
        <button type="submit">Entrar</button>
      </form>
      <p v-if="error">{{ error }}</p>
    </div>
</template>
  
  <script setup>
  import { ref } from 'vue';
  import { login } from '@/stores/authService';
  import { useRouter } from 'vue-router';
  import { useAuthStore } from '@/stores/authService';
  
  const email = ref('');
  const password = ref('');
  const error = ref('');
  const router = useRouter();

  const authStore = useAuthStore();
  
  const handleLogin = async () => {
    try {
      const response = await login(email.value, password.value);
      const usuario = response.usuario
      authStore.iniciarSesion(response.token, usuario.id, usuario.nombre, usuario.email) //llama al metodo que carga los datos del usuario en el localstorage
      router.push('/'); // Redirigir tras login al viewhome
    } catch (err) {
      console.error('Error al iniciar sesión:', err)
      error.value = 'Credenciales inválidas';
    }
  };
  </script>