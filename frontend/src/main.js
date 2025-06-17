import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import 'vuetify/styles'
import PrimeVue from 'primevue/config'
import { useAuthStore } from './stores/authService'
import { carroCompraStore } from './stores/carroCompras'

import 'primeicons/primeicons.css'
import 'primeflex/primeflex.css'

const vuetify = createVuetify({
  components,
  directives,
  theme: {
    defaultTheme: 'light',
    themes: {
      light: {
        colors: {
          primary: '#855cad',  // púrpura
          secondary: '#7fa8d1',// azul suave
          background: '#ffffff'
        }
      }
    }
  }
})

import App from './App.vue'
import router from './router'
import './assets/main.css'

const pinia = createPinia()
const app = createApp(App)

app.use(pinia)
app.use(router)
app.use(vuetify)
app.use(PrimeVue)

app.mount('#app')

const authStore = useAuthStore()
await authStore.cargarSesion()

const carroStore = carroCompraStore()
await carroStore.bajarCarroStorage(authStore.id, authStore.token)
