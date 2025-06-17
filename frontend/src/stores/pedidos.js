import axios from 'axios';
import { defineStore } from 'pinia'

const API = 'http://127.0.0.1:5000/pedido';


export const pedidoStore = defineStore('pedido', {
    actions:{
        async crearPedido(nombreUsuario, email, telefono, direccion, detalleDireccion, cedula, idCarroCom){
            await axios.post(`${API}/`, {nombreUsuario, email, telefono, direccion, detalleDireccion, cedula, idCarroCom });
        }
    }
})