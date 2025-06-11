import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import axios from 'axios'

const API = 'http://localhost:5000/item_carro';

const images = import.meta.glob('@/assets/*', {
  eager: true,
  import: 'default',
  query: '?url'
})

export const actualizarCantidadItem = async (idItem, idCarro, idProductos, cantidad) => {
 await axios.put(`${API}/${idItem}`, {idCarro, idProductos, cantidad});
}

export const crearItemCarro = async (idCarro, idProductos, cantidad) => {
  const res = await axios.post(`${API}/`, {idCarro, idProductos,cantidad});
  return res.data;
 }

export const useCartStore = defineStore('cart', () => {
  const items = ref([])

  const resolveImage = (filename) => images[`/src/assets/${filename}`] || ''


  const cargarCarrito = async (idCarro) => {
    await axios.get(`${API}/por-carro/${idCarro}`)
      .then(res => {
        const items = res.data.map(item => ({
          id: item.id,
          idProduct: item.idProductos,
          name: item.nombre,
          quantity: item.cantidad,
          price: item.precio,
          image: item.imagenPrin,
          description: item.descripcion,
          stock: item.stock,
          idCarro: item.idCarro
        }))
        setItems(items)
      })
      .catch(err => {
        console.error('Error al cargar carrito:', err)
      })
  }


  const addToCart = async (product, idCarro, cantidad) => {
    const existing = items.value.find(item => item.idProduct === product.id)
    if (existing) {
      const nuevaCantidad = existing.quantity + cantidad
      existing.quantity = nuevaCantidad
      try {
        await actualizarCantidadItem(existing.id,existing.idCarro,existing.idProduct,nuevaCantidad
        )
      } catch (e) {
        console.error('Error actualizando cantidad en API:', e)
      }
    } else {
      const data = await crearItemCarro(idCarro, product.id, cantidad)
      items.value.push({
        id: data.id,
        idProduct: product.id,
        name: product.nombre,
        quantity: cantidad,
        price: product.precio,
        image: resolveImage(product.imagenPrin),
        description: product.descripcion,
        stock: product.stock,
        idCarro: idCarro
      })
    }
  }

  const clearCart = () => {
    items.value = []
  }


  const setItems = (newItems) => {
    items.value = newItems.map(item => ({
      ...item,
      image: resolveImage(item.image)
    }))
  }

  const subtotal = computed(() =>
    items.value.reduce((acc, item) => acc + item.quantity * item.price, 0)
  )

  return {
    items,
    addToCart,
    clearCart,
    setItems,
    subtotal,
    cargarCarrito
  }
})