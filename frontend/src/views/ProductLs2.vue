<script setup>
import Carousel from 'primevue/carousel';
import Tag from 'primevue/tag';
import Button from 'primevue/button';

// Datos de prueba
const products = [
  { name: "Producto 1", price: 99.99, image: "bamboo-watch.jpg", inventoryStatus: "INSTOCK" },
  { name: "Producto 2", price: 129.99, image: "blue-band.jpg", inventoryStatus: "LOWSTOCK" },
  { name: "Producto 3", price: 59.99, image: "game-controller.jpg", inventoryStatus: "OUTOFSTOCK" }
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
            <div class="relative mx-auto">
              <img :src="'https://primefaces.org/cdn/primevue/images/product/' + slotProps.data.image" 
                   :alt="slotProps.data.name" class="w-full rounded" />
              <Tag :value="slotProps.data.inventoryStatus" :severity="getSeverity(slotProps.data.inventoryStatus)" 
                   class="absolute" style="left:5px; top: 5px"/>
            </div>
          </div>
          <div class="mb-4 font-medium">{{ slotProps.data.name }}</div>
          <div class="flex justify-between items-center">
            <div class="mt-0 font-semibold text-xl">${{ slotProps.data.price }}</div>
            <span>
              <Button icon="pi pi-heart" severity="secondary" outlined />
              <Button icon="pi pi-shopping-cart" class="ml-2"/>
            </span>
          </div>
        </div>
      </template>
    </Carousel>
</template>
