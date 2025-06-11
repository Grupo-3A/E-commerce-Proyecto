<template>
  <section class="inventario-container">

    <div v-if="isLoading" class="grid-5col">
      <div
        v-for="n in 5"
        :key="n"
        class="skeleton-card">

        <div class="skeleton-img"></div>
        <div class="skeleton-line short"></div>
        <div class="skeleton-line medium"></div>
        <div class="skeleton-line text"></div>
      </div>
    </div>


    <div v-else class="grid-5col" :style="gridStyles">
      <div
        v-for="producto in productosVisibles"
        :key="producto.id"
        class="grid-item"
      >
        <ProductoCard :producto="producto" />
      </div>
    </div>


    <div
      v-if="!isLoading && visibleCount < inventario.productos.length"
      class="load-more-container"
    >
      <button @click="cargarMas" class="btn-cargar-mas">
        Cargar más
      </button>
    </div>
  </section>
</template>

<script setup>
import { ref, computed, onMounted, watch, nextTick } from 'vue';
import { useProductoStore } from '@/stores/Productos';
import ProductoCard from '@/components/ProductoCard.vue';

const inventario = useProductoStore();

const visibleCount = ref(5);
const isLoading = ref(true);

const productosVisibles = computed(() =>
  inventario.productos.slice(0, visibleCount.value)
);

let observer = null;

function cargarMas() {
  visibleCount.value += 5;
}

// 5) Configura IntersectionObserver sobre el último elemento .grid-item
async function setupObserver() {
  await nextTick();
  const ultimaCard = document.querySelector('.grid-item:last-child');
  if (!ultimaCard) return;

  observer = new IntersectionObserver(entries => {
    if (
      entries[0].isIntersecting &&
      visibleCount.value < inventario.productos.length
    ) {
      cargarMas();
    }
  });
  observer.observe(ultimaCard);
}

onMounted(async () => {
  isLoading.value = false;
  setupObserver();
});

// 8) Cuando visibleCount cambia (“cargamos más”), volvemos a configurar el observer
watch(visibleCount, async () => {
  if (!isLoading.value) {
    if (observer) observer.disconnect();
    await setupObserver();
  }
});

const gridStyles = computed(() => {
  const n = productosVisibles.value.length
  if (n < 5) {
    return {
      gridTemplateColumns: `repeat(${n}, 300px)`,
      justifyContent: 'center'
    }
  } else {
    return {
      gridTemplateColumns: `repeat(5, 1fr)`,
      justifyContent: 'start'
    }
  }
})
</script>

<style scoped>

.inventario-container {
  width: 95vw;
  padding: 1rem;
  margin-top: 160px;
  margin-bottom: 280px;
  height: 1200px;
  display: flex;
  justify-content: center;
  margin-left: 2vw;
}

.grid-5col {
  display: grid;
  gap: 1rem; 
  margin: 0 auto;
  grid-auto-rows: auto;
  align-content: start;
}

.grid-item {
  display: flex;        
  flex-direction: column;
  margin-top: 20px;
}


.load-more-container {
  margin-top: 1.5rem; 
  text-align: center;
}
.btn-cargar-mas {
  background-color: #3b82f6;      
  color: white;
  padding: 0.5rem 1rem;           
  border-radius: 0.375rem;        
  font-weight: 500;
  cursor: pointer;
  border: none;
}
.btn-cargar-mas:hover {
  background-color: #2563eb;      
}

/* ==============================
   Estilos para Skeleton (Esqueleto)
   ============================== */
.skeleton-card {
  border: 1px solid #e2e8f0; 
  border-radius: 0.75rem;    
  padding: 1rem;              
  height: 500px;              
  display: flex;
  flex-direction: column;
}
.skeleton-img {
  background-color: #e2e8f0;  
  height: 10rem;               
  border-radius: 0.5rem;       
  margin-bottom: 0.5rem;      
}
.skeleton-line {
  background-color: #e2e8f0;
  border-radius: 0.25rem;      
  margin-bottom: 0.5rem;      
}
.skeleton-line.short { width: 75%; height: 1rem; }
.skeleton-line.medium { width: 50%; height: 1rem; }
.skeleton-line.text { width: 35%; height: 1.5rem; }
</style>