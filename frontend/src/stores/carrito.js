import { defineStore } from 'pinia'
import { ref, computed } from 'vue'



export const useCartStore = defineStore('cart', () => {
  const items = ref([])

  const addToCart = (product) => {
    const existing = items.value.find(item => item.name === product.name)
    if (existing) {
      existing.quantity += product.quantity
    } else {
      const imageUrl = new URL(`@/assets/images/${product.image}`, import.meta.url).href
      items.value.push({ ...product, image: imageUrl })
    }
  }

  const clearCart = () => {
    items.value = []
  }

  const subtotal = computed(() =>
    items.value.reduce((acc, item) => acc + item.quantity * item.price, 0)
  )

  return {
    items,
    addToCart,
    clearCart,
    subtotal
  }
})
