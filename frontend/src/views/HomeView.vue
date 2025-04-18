<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const irAProducto1 = () => {
  router.push('/ProductLs2')
}

const irAProducto2 = () => {
  router.push('/ProductShaft')
}

const irAProducto3 = () => {
  router.push('/ProductAgv')
}
</script>

<template>
  <div class="full-width-container">
    <div class="image-container">
      <img src="@/assets/coraje.png" alt="Casco Coraje" class="full-width-image">
    </div>

    <div class="botones-wrapper">
      <div class="botones-container">
        <v-btn @click="irAProducto1" elevation="24" class="boton-marca">
          <img class="shift" src="@/assets/ls2.png" alt="LS2">
        </v-btn>
        <v-btn @click="irAProducto2" elevation="24" class="boton-marca">
          <img class="shift" src="@/assets/shaft.png" alt="Shaft">
        </v-btn>
        <v-btn @click="irAProducto3" elevation="24" class="boton-marca">
          <img class="agv" src="@/assets/agv.png" alt="AGV">
        </v-btn>
      </div>
    </div>
  </div>
</template>


<style scoped>

  /* Contenedor general */
  .full-width-container {
    width: 100vw;
    height: 1200px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    overflow-x: hidden;
    margin: 0 !important;
    padding: 0 !important; /* Asegurar que no haya espacio extra */
    position: relative;
    margin-top: 280px;
  }
  /* Contenedor de la imagen */
  .image-container {
    width: 100vw;
    max-width: 100vw;
    height: 800px;
    display: flex;
    justify-content: flex-start;
    align-items: center;
    margin: 0;
    padding: 0;
  }

  /* Imagen */
  .full-width-image {
    width: 100%;
    max-width: 100vw; /* Asegura que la imagen no se desborde */
    height: 800px;
    display: block;
    object-fit: cover;
    margin-top: 148px;
    position: relative; /* Evita desplazamientos por herencias */
    left: 0; /* Asegura que no se mueva a la derecha */
    right: 0;
  }

  /* Contenedor de botones */
  .botones-wrapper {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;

  }

  /* Caja de botones */
  .botones-container {
    width: 100%;
    height: 400px;
    max-width: 2000px;
    display: flex;
    justify-content: space-around;
    align-items: center;
    background-color: rgb(27, 22, 22);

    border-radius: 0px;
    gap: 20px;
    flex-wrap: wrap;
  }

  /* Botones individuales */
  .boton-marca {
    width: 500px;
    max-width: 500px;
    height: 130px;
    display: flex;
    justify-content: center;
    align-items: center;
    background: linear-gradient(45deg, #389dcc, #a244aa);
    color: white;
    flex-shrink: 0;
  }

  .shift {
    width: 300px;
    height: 300px;
    object-fit: contain;
  }

  .agv {
    width: 200px;
    height: 150px;
    object-fit: contain;
  }
  </style>