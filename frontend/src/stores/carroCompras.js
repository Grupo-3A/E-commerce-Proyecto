import axios from 'axios';
import { defineStore } from 'pinia'

const API = 'http://127.0.0.1:5000/carro_compras';

export const crearCarro = async (idUsuario) => {
    const subtotal = 0.0;
    const res = await axios.post(`${API}/`, {idUsuario, subtotal });
    return res.data;
};

export const actualizarCarro = async (idCarro, idUsuario,subtotal) => {
    const res = await axios.put(`${API}/${idCarro}`, {idUsuario, subtotal});
    return res.data;
};

export const carroCompraStore = defineStore('carroCompras', {
    state: () => ({
      id: null,
      subtotal: null,
      usuario: null,
    }),
    actions: {
      async crearCarroStore(idUsuario){
        const respuesta = await crearCarro(idUsuario);        
        this.subirCarroStorage(respuesta.idCarro, respuesta.subtotal);
      },
      subirCarroStorage(id, subtotal) {
        this.id = id
        this.subtotal = subtotal
        // Guardar en localStorage
        localStorage.setItem('idCarroCompras', JSON.stringify(id))
        localStorage.setItem('subtotal', JSON.stringify(subtotal))
      },
      async borrarCarroStorage() {
        this.id = null
        this.subtotal = null
        localStorage.removeItem('idCarroCompras')
        localStorage.removeItem('subtotal')
      },
      async bajarCarroStorage(idUsuario, token) {
        const id = localStorage.getItem('idCarroCompras')
        const subtotal = localStorage.getItem('subtotal')
        if ( id && subtotal ){
            if ( !tokenExpirado(token)) {
                this.id = JSON.parse(id)
                this.subtotal = JSON.parse(subtotal)
            }else {
                this.borrarCarroStorage()
            }
        }else{
             const respuesta = await crearCarro(idUsuario);        
             this.subirCarroStorage(respuesta.idCarro, respuesta.subtotal);
        }
      },
      async actualizarCarroCompras(idCarro, usuario, subtotal){
        this.subirCarroStorage(idCarro, subtotal)
        try {
          await actualizarCarro(idCarro, usuario, subtotal)
        } catch (e) {
          console.error('Error actualizando subtotal en API:', e)
        }
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
