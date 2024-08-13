<script setup>
</script>

<template>
  <!-- Content -->
  <div class="main">
    <router-view></router-view>
  </div>

  <!-- Footer -->
  <footer class="bg-primary texte-light">
    <p class="text-white">Feito com carinho por Gabriel Eduardo</p>
  </footer>
</template>

<style scoped>
footer {
  position: fixed;
  bottom: 0;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 56px;
}
</style>
