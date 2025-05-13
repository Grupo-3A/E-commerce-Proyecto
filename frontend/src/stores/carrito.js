import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

const images = import.meta.glob('@/assets/*', {
  eager: true,
  import: 'default',
  query: '?url'
})

export const useCartStore = defineStore('cart', () => {
  const items = ref([])

  const addToCart = (product) => {
    const existing = items.value.find(item => item.name === product.name)
    if (existing) {
      existing.quantity += product.quantity
    } else {
      const imageUrl = images[`/src/assets/${product.image}`]
      console.log('Imagen resuelta:', imageUrl)
      items.value.push({ ...product, image: imageUrl })
    }
  }

  const clearCart = () => {
    items.value = []
  }

  const setItems = (newItems) => {
    const imageUrl = images[`/src/assets/${newItems.image}`]
    console.log('Imagen resuelta:', imageUrl)
    items.value.push({ ...newItems, image: imageUrl })
    items.value = newItems
  }

  const subtotal = computed(() =>
    items.value.reduce((acc, item) => acc + item.quantity * item.price, 0)
  )

  return {
    items,
    addToCart,
    clearCart,
    setItems,
    subtotal
  }
})