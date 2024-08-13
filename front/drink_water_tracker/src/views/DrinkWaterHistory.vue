<template>
  <div class="container d-flex justify-content-center align-items-center flex-column p-5 gap-5">
    <section class="d-flex justify-content-center align-items-center flex-column gap-2">
      <h2 class="card-title mb-1 text-center text-primary">Histórico</h2>
      <h3 class="fs-5 mb-1 text-center text-primary-emphasis">Usuário: {{user.name}}</h3>
      <button type="button" class="btn btn-primary" @click="go_home()">Voltar</button>
    </section>

    <section v-for="goal in historyGoals" :key="goal.id" >
        <div class="card" style="width: 20rem;">
          <div class="card-header">
            Data: {{goal.date}}
          </div>
          <ul class="list-group list-group-flush">
            <li class="list-group-item">Meta: {{user.daily_goal}}</li>
            <li class="list-group-item">ml consumida: {{goal.total_consumption}}</li>
            <li class="list-group-item">Chegou na meta? {{goal.goal_achieved ? 'Sim':'Não'}}</li>
          </ul>
        </div>
    </section>
  </div>
</template>

<script setup>
import { onMounted, computed } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'

const router = useRouter()

const store = useStore()
const { state, dispatch } = store


const user = computed(() => state.user)
const historyGoals = computed(() => store.state.historyGoals)

const fetchHistoryGoals = async () => {
  if (user.value && user.value.id) {
    try {
      await dispatch('fetchHistoryGoals')
    } catch (error) {
      console.error('Erro ao buscar o histórico de metas:', error)
    }
  } else {
    console.error('Usuário não definido ou não possui ID')
  }
}

onMounted(fetchHistoryGoals)

const go_home = () => {
    router.push('/home')
  }

</script>
