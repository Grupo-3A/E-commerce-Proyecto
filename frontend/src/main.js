import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import 'vuetify/styles'
import PrimeVue from 'primevue/config'

// Estilos de PrimeVue
import 'primeicons/primeicons.css'  // Iconos de PrimeVue

import App from './App.vue'
import router from './router'
import './assets/main.css'

const vuetify = createVuetify({
  components,
  directives,
})

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(vuetify)
app.use(PrimeVue)

app.mount('#app')
