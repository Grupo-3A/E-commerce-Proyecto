import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

const images = import.meta.glob('@/assets/*', {
  eager: true,
  import: 'default',
  query: '?url'
})

export const useCartStore = defineStore('cart', () => {
  const items = ref([])


  const resolveImage = (filename) => images[`/src/assets/${filename}`] || ''

  const addToCart = (product) => {
    const existing = items.value.find(item => item.name === product.name)
    if (existing) {
      existing.quantity += product.quantity
    } else {
      items.value.push({ ...product, image: resolveImage(product.image) })
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
    subtotal
  }
})