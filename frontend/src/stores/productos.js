import axios from 'axios';
import { defineStore } from 'pinia'

const images = import.meta.glob('@/assets/*', {
    eager: true,
    import: 'default',
    query: '?url'
  })

const resolveImage = (filename) => images[`/src/assets/${filename}`] || ''
  

const API = 'http://localhost:5000/productos/';


export const getProductos = () => axios.get(`${API}`);

export const getProductoPorId = (id) => axios.get(`${API}${id}`);

export const getProductosPorCategoria = (idCategoria) =>
  axios.get(`${API}categoria/${idCategoria}`);

export const getProductosPorMarca = (idMarca) =>
  axios.get(`${API}marca/${idMarca}`);

export const getFavoritosPorId = (id) => 
  axios.get(`http://localhost:5000/favoritos/obtener-favoritos/${id}`);


export const useProductoStore = defineStore('producto',{
    state: () => ({
        productoActual: null,
        productos: [],
    }),
    actions: {
          async cargarProductos(search = '') {
            try {
              const params = search.trim() ? { search } : {}
              const response = await axios.get(API, { params })
              this.productos = response.data.map(item => ({
                ...item,
                imagenPrin: resolveImage(item.imagenPrin)
              }))
              return this.productos
            } catch (error) {
              console.error('Error cargando productos:', error)
              return []
            }
          },
      
          async cargarProductosPorCategoria(idCategoria) {
            try {
              const response = await getProductosPorCategoria(idCategoria);
              this.productos = response.data.map(item => ({
                ...item,
                imagenPrin: resolveImage(item.imagenPrin)
              }));
            } catch (error) {
              console.error('Error cargando productos por categoría:', error);
            }
          },

          async cargarProductosPorMarca(idMarca) {
            try {
              const response = await getProductosPorMarca(idMarca);
              this.productos = response.data.map(item => ({
                ...item,
                imagenPrin: resolveImage(item.imagenPrin)
              }));
            } catch (error) {
              console.error('Error cargando productos por marca:', error);
            }
          },
    
          async cargarProducto(id) {
            try {
              const response = await getProductoPorId(id);
              const prodObj = Array.isArray(response.data)
                ? response.data[0]
                : response.data;
                
              this.productoActual = {
                ...prodObj,
                imagenPrin: resolveImage(prodObj.imagenPrin)
              };
            } catch (error) {
              console.error('Error cargando producto:', error);
            }
          },

          async cargarFavoritos(id) {
            try {
              const response = await getFavoritosPorId(id);
              this.productos = response.data.map(item => ({
                ...item,
                imagenPrin: resolveImage(item.imagenPrin)
              }));
            } catch (error) {
              console.error('Error cargando favoritos:', error);
            }
          }
    }

} )