<template>
  <form @submit.prevent="handleSubmit">
    <div class="d-flex flex-column justify-content-center align-items-center">
      <div class="card" style="width: 18rem;">
        <div class="card-header">
          Quantas ML você bebeu
        </div>
        <div class="d-flex p-2">
          <label for="ml" class="visually-hidden">ML consumidos</label>
          <input
            type="number"
            id="ml"
            class="form-control"
            v-model="ml"
            required
            aria-label="Quantidade de água consumida em mililitros"
          />
          <button type="submit" class="btn btn-primary ms-2">Consumir</button>
        </div>
      </div>
    </div>
  </form>
</template>

<script setup>
import { ref, computed } from 'vue'
import axios from 'axios'
import { useStore } from 'vuex'
import { format } from 'date-fns'


const ml = ref('')
const store = useStore()
const { state, dispatch } = store

const handleSubmit = async () => {
  try {
    const current_date = format(new Date(), 'yyyy-MM-dd')
    const userData = {
      quantity_ml: ml.value,
      date_drink_water: current_date,
      user: state.user.id
    }

    await axios.post('/api/drink_waters/', userData)
    await dispatch('fetchDailyGoals')

    ml.value = ''
  } catch (error) {
    console.error('Erro ao registrar o consumo de água:', error)
  }
}
</script>
