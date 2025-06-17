import axios from 'axios';
import { defineStore } from 'pinia'

const API = 'http://localhost:5000/usuarios';

export const login = async (email, password) => {
  const res = await axios.post(`${API}/login`, { email, password });
  return res.data;
};

export const register = async (usuario) => {
  const res = await axios.post(`${API}/`, usuario);
  return res.data;
};

export const invitado = async () => {
  const res = await axios.post(`${API}/tokenNoUser`);
  return res.data;
};

export const buscarUsuario = async (idUsuario) => {
  const res = await axios.get(`${API}/${idUsuario}`);
  return res.data;
};

export const useAuthStore = defineStore('auth', {
    state: () => ({
      token: null,
      id: null,
      usuario: null,
      email: null,  
    }),
    actions: {
      iniciarSesion(token, id, usuario, email) {
        this.token = token
        this.usuario = usuario
        this.email = email
        this.id = id
        // Guardar en localStorage
        localStorage.setItem('token', token)
        localStorage.setItem('usuario', JSON.stringify(usuario))
        localStorage.setItem('email', JSON.stringify(email))
        localStorage.setItem('id', JSON.stringify(id))
      },
      cerrarSesion() {
        this.token = null
        this.id = null
        this.usuario = null
        this.email = null
        localStorage.removeItem('token')
        localStorage.removeItem('id')
        localStorage.removeItem('usuario')
        localStorage.removeItem('email')
      },
      async cargarSesion() {
        const token = localStorage.getItem('token')
        const id = localStorage.getItem('id')
        const usuario = localStorage.getItem('usuario')
        const email = localStorage.getItem('email')
        if (token && usuario && email && id && !tokenExpirado(token)) {
          this.token = token
          this.id = JSON.parse(id)
          this.usuario = JSON.parse(usuario)
          this.email = JSON.parse(email)
        }else if(token && usuario && !tokenExpirado(token)){
          this.token = token
          this.usuario = JSON.parse(usuario)
        }else if(token == null){
          const response =  await invitado()
          this.token = response.token;
          this.usuario = response.guestId;
          localStorage.setItem('token', response.token)
          localStorage.setItem('usuario', JSON.stringify(response.guestId))
        }else{
            this.cerrarSesion()
            const response =  await invitado()
            this.token = response.token;
            this.usuario = response.guestId;
            localStorage.setItem('token', response.token)
            localStorage.setItem('usuario', JSON.stringify(response.guestId))
        }
      },
      async consultarUsuario(idUsuario){
          const response = await buscarUsuario(idUsuario);
          return response
      }
    }
  })


  function tokenExpirado(token) {
    try {
      const payload = JSON.parse(atob(token.split('.')[1]))
      const exp = payload.exp
      const now = Math.floor(Date.now() / 1000)
      return now > exp
    } catch (e) {
        console.error('Token Expiro:', e)
      return true // Token inválido
    }
  }

