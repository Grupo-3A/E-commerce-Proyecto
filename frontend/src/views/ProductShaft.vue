<script setup>
import Carousel from 'primevue/carousel';
import Tag from 'primevue/tag';
import Button from 'primevue/button';

import casco1 from '@/assets/Shaft 520 Evo Reptile.webp';
import casco2 from '@/assets/Shaft 541 Pro Flash.webp';
import casco3 from '@/assets/Shaft 598 DV Carbon Storm.webp';


// Datos de prueba
const products = [

  { name: "Shaft 520 Evo Reptile",price: 150.00,image: casco1,inventoryStatus: "INSTOCK"},
  { name: "Shaft 541 Pro Flash", price: 180.00, image: casco2, inventoryStatus: "LOWSTOCK" },
  { name: "Shaft 598 DV Carbon Storm", price: 250.00, image: casco3, inventoryStatus: "OUTOFSTOCK" }
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
      <div class="border border-surface-200 dark:border-surface-700 rounded m-2 p-4">
        <div class="mb-4">
          <div class="relative mx-auto overflow-hidden rounded">
            <img
              :src="slotProps.data.image"
              :alt="slotProps.data.name"
              class="w-full h-60 object-cover transition-transform duration-300 hover:scale-105"
            />
            <Tag
              :value="slotProps.data.inventoryStatus"
              :severity="getSeverity(slotProps.data.inventoryStatus)"
              class="absolute"
              style="left:5px; top: 5px"
            />
          </div>
        </div>
        <div class="mb-4 font-medium text-center">{{ slotProps.data.name }}</div>
        <div class="flex justify-between items-center">
          <div class="font-semibold text-xl text-blue-400">${{ slotProps.data.price }}</div>
          <span>
            <Button icon="pi pi-heart" severity="secondary" outlined />
            <Button icon="pi pi-shopping-cart" class="ml-2" />
          </span>
        </div>
      </div>
    </template>
  </Carousel>
</template>