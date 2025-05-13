<script setup>
import Carousel from 'primevue/carousel';
import Tag from 'primevue/tag';
import Button from 'primevue/button';

import casco1 from '@/assets/AGV K1 S Power.webp';
import casco2 from '@/assets/AGV K3 Rossi Misano.webp';
import casco3 from '@/assets/AGV Pista GP RR Limited Edition Winter Test.webp';


// Datos de prueba
const products = [

  { name: "AGV K1 S Power",price: 150.00,image: casco1,inventoryStatus: "INSTOCK"},
  { name: "AGV K3 Rossi Misano", price: 180.00, image: casco2, inventoryStatus: "LOWSTOCK" },
  { name: "AGV Pista GP RR Limited Edition Winter Test", price: 250.00, image: casco3, inventoryStatus: "OUTOFSTOCK" }
];


// Opciones responsivas para el carrusel
const responsiveOptions = [
  { breakpoint: '1024px', numVisible: 3, numScroll: 3 },
  { breakpoint: '768px', numVisible: 2, numScroll: 2 },
  { breakpoint: '560px', numVisible: 1, numScroll: 1 }
];

// Método para determinar el color del tag
const getSeverity = (status) => {
  switch (status) {
    case "INSTOCK": return "success";
    case "LOWSTOCK": return "warning";
    case "OUTOFSTOCK": return "danger";
    default: return null;
  }
};
</script>

<template>
  <Carousel :value="products" :numVisible="3" :numScroll="3" :responsiveOptions="responsiveOptions">
    <template #item="slotProps">
      <div class="border border-surface-200 dark:border-surface-700 rounded m-2 p-4 flex flex-col h-full min-h-[420px] shadow-md">

        <!-- Imagen con tamaño fijo y centrada -->
        <div class="relative w-full h-60 flex items-center justify-center mb-4">
          <img :src="slotProps.data.image" :alt="slotProps.data.name"
               class="max-h-full max-w-full object-contain rounded" />
          <Tag :value="slotProps.data.inventoryStatus" 
               :severity="getSeverity(slotProps.data.inventoryStatus)" 
               class="absolute left-2 top-2"/>
        </div>

        <!-- Contenido de texto centrado -->
        <div class="flex-1 flex flex-col justify-between text-center px-2">
          <div class="font-semibold text-lg mb-2">
            {{ slotProps.data.name }}
          </div>
          <div class="text-xl font-bold text-primary mb-4">
            ${{ slotProps.data.price }}
          </div>

          <!-- Botones alineados abajo -->
          <div class="flex justify-center gap-3 mt-auto">
            <Button icon="pi pi-heart" severity="secondary" outlined />
            <Button icon="pi pi-shopping-cart" />
          </div>
        </div>

      </div>
    </template>
  </Carousel>
</template>