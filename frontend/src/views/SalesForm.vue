<script setup>
import { ref, computed } from 'vue'
import { useCartStore } from '@/stores/carrito'

const cart = useCartStore()

const step = ref(1)
const shipping = ref(0)

const subtotal = computed(() => cart.subtotal)
const total = computed(() => subtotal.value + Number(shipping.value ?? 0))
const products = computed(() => cart.items)

const items = [
  'Revisar Orden',
  'Informacion de Envio',
  'Confirmacion',
]

  const email = ref('')

  const rules = {
    required: value => !!value || 'Required.',
    email: value => {
      const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
      return pattern.test(value) || 'Invalid e-mail.'
    },
  }

</script>


<template>
    <v-container
      fluid
      style="min-height: calc(100vh - 400px)" 
      class="centrar-stepper"
    >
      <v-sheet
        class="pa-4"
        elevation="2"
        max-width="1200"
        width="100%"
      >
        <v-stepper
          v-model="step"
          :items="items"
          show-actions
        >
          <!-- Paso 1 -->
          <template v-slot:item.1>
            <h3 class="text-h6">Order</h3>
            <br />
            <v-sheet border>
              <v-table>
                <thead>
                  <tr>
                    <th>Producto</th>
                    <th class="text-end">Cantidad</th>
                    <th class="text-end">Precio</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(product, index) in products" :key="index">
                      <td>
                        <v-row align="center" no-gutters>
                          <v-col cols="4">
                            <v-img
                              :src="product.image"
                              width="60"
                              height="60"
                              cover
                              class="rounded"
                            />
                          </v-col>
                          <v-col cols="8">
                            {{ product.name }}
                          </v-col>
                        </v-row>
                      </td>
                      <td class="text-end">{{ product.quantity }}</td>
                      <td class="text-end">{{ product.quantity * product.price }}</td>
                    </tr>
                  <tr>
                    <th>Total</th>
                    <th></th>
                    <th class="text-end">${{ subtotal }}</th>
                  </tr>
                </tbody>
              </v-table>
            </v-sheet>
          </template>
  
          <!-- Paso 2 -->
          <template v-slot:item.2>
            <h3 class="text-h6">Shipping</h3>
            <br />
            <v-col
            
              sm="6"
            >
              <v-text-field
                :rules="[rules.required]"
                label="Nombre"
                variant="solo"
              ></v-text-field>
            </v-col>

            <v-col
            
              sm="6"
            >
              <v-text-field
                v-model="email"
                :rules="[rules.required, rules.email]"
                label="E-mail"
                variant="solo"
              ></v-text-field>
            </v-col>

            <v-col
   
              sm="6"
            >
              <v-text-field
                :rules="[rules.required]"
                label="Telefono"
                variant="solo"
              ></v-text-field>
            </v-col>

            <v-row class="margin_left">
            <v-col
              sm="6"
            >
              <v-text-field
                :rules="[rules.required]"
                label="Direccion"
                append-icon="mdi-map-marker"
                variant="solo"
              ></v-text-field>
            </v-col>

            <v-col
              
              sm="5"
            >
              <v-text-field
               
                :rules="[rules.required]"
                label="Detalle de Direccion (apt, edificio, conjunto, etc)"
                class="margin_left"
                variant="solo"
              ></v-text-field>
            </v-col>
          </v-row>

            <v-col
              cols="12"
              sm="6"
            >
              <v-text-field
              
                :rules="[rules.required]"
                label="Documento de Identidad"
                variant="solo"
              ></v-text-field>
            </v-col>
 
          </template>
  
          <!-- Paso 3 -->
          <template v-slot:item.3>
            <h3 class="text-h6">Confirmacion</h3>
            <br />
            <v-sheet border>
              <v-table>
                <thead>
                  <tr>
                    <th>Descripcion</th>
                    <th class="text-end">Cantidad</th>
                    <th class="text-end">Precio</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(product, index) in products" :key="index">
                    <td>{{ product.name }}</td>
                    <td class="text-end">{{ product.quantity }}</td>
                    <td class="text-end">{{ product.quantity * product.price }}</td>
                  </tr>
                  <tr>
                    <td>Envio</td>
                    <td></td>
                    <td class="text-end">${{ shipping }}</td>
                  </tr>
                  <tr>
                    <th>Total</th>
                    <th></th>
                    <th class="text-end">${{ total }}</th>
                  </tr>
                </tbody>
              </v-table>
            </v-sheet>
          </template>
        </v-stepper>
      </v-sheet>
    </v-container>
  </template>


<style scoped>
 .centrar-stepper {
    width: 100vw;
    display: flex;
    justify-content: center;
    margin-top: 128px;
  }

  .v-text-field {
  height: 70px;
}

  .margin_left{
    margin-left: 0px;
  } 
</style>