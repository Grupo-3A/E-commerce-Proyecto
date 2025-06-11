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


export const useProductoStore = defineStore('producto',{
    state: () => ({
        productoActual: null,
        productos: [],
        categorias: [],
        marcas: []
    }),
    actions: {
          async cargarProductos() {
            try {
              const response = await getProductos();
              this.productos = response.data.map(item => ({
                ...item,
                imagenPrin: resolveImage(item.imagenPrin)
              }));
            } catch (error) {
              console.error('Error cargando productos:', error);
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
          }
    }

} )