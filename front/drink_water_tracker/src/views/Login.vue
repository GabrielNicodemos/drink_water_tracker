<template>
  <div class="container d-flex justify-content-center align-items-center min-vh-100">
    <div class="card p-4 shadow-sm" style="max-width: 400px; width: 100%;">
      <h3 class="card-title mb-1 text-center text-primary">Entre e faça suas ingessões de água</h3>
      <p class="text-center text-primary-emphasis">Sua saúde agradece</p>
      <form @submit.prevent="handleSubmit">
        <div class="mb-3">
          <label for="name" class="form-label">Name</label>
          <input
            type="text"
            id="name"
            class="form-control"
            v-model="name"
            required
          />
        </div>
        <div class="mb-3">
          <label for="weight" class="form-label">Weight (kg)</label>
          <input
            type="number"
            id="weight"
            class="form-control"
            v-model="weight"
            required
          />
        </div>
        <button type="submit" class="btn btn-primary">Entrar</button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'
import { useStore } from 'vuex'


const name = ref('')
const weight = ref('')
const router = useRouter()
const store = useStore()

const handleSubmit = async () => {
  try {
    const userData = { name: name.value, weight: weight.value }
    await store.dispatch('login', userData)

    router.push('/home')
  } catch (error) {
    console.error('Error logging in:', error)
  }
}
</script>

<style scoped>
.min-vh-100 {
  min-height: 100vh;
}
</style>
