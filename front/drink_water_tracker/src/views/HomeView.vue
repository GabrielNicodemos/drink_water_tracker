<template>
  <div v-if="user" class="container text-center justify-content-center align-items-center p-5 gap-5">
      <div class="col mb-5" >
          <h3 class="card-title mb-1 text-center text-primary">Data de hoje: 08/01/2023</h3>
      </div>
      <div class="col mb-5">
        <DrinkWater />
      </div>
      <div class="col mb-5">
        <DailyGoalsView />
      </div>
      <div class="col mb-5">
        <button type="btn" class="btn btn-primary" @click="go_history()">Histórico</button>
      </div>
  </div>
  <div v-else class="container text-center justify-content-center align-items-center min-vh-100r p-5 gap-5">
    <h2 class="card-title mb-1 text-center text-primary">Que Pena :(</h2>
    <h3 class="fs-5 mb-1 text-center text-primary-emphasis">Você foi desconectar</h3>
    <button type="button" class="btn btn-primary" @click="go_login()">Voltar Login</button>
  </div>
</template>

<script setup>
  import { computed } from 'vue'
  import { useRouter } from 'vue-router'
  import DailyGoalsView from '../components/DailyGoalsView.vue';
  import DrinkWater from '../components/DrinkWater.vue';
  import { useStore } from 'vuex'

  const router = useRouter()

  const store = useStore()
  const { state, dispatch } = store
  const user = computed(() => state.user)

  const go_history = () => {
    router.push('/history')
  }

  const go_login = () => {
    router.push('/')
  }

</script>
