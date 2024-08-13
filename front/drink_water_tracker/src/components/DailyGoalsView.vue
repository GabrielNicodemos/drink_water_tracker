<template>
  <div class="d-flex justify-content-center align-items-center">
      <div class="card" style="width: 18rem;" >
        <div class="card-header">
          {{ hasDailyGoals ? 'Métricas do dia' : 'Você ainda não bebeu água hoje :(' }}
        </div>
        <ul v-if="hasDailyGoals" class="list-group list-group-flush">
          <li class="list-group-item">Meta do Dia (ML): {{ user.daily_goal }}</li>
          <li class="list-group-item">Meta restante (ML): {{ remainingGoal }}</li>
          <li class="list-group-item">Meta já consumida (ML): {{ totalConsumption }}</li>
          <li class="list-group-item">Meta já consumida (%): {{ consumptionPercentage }}%</li>
          <li class="list-group-item">{{ goalStatusMessage }}</li>
        </ul>
      </div>
  </div>
</template>

<script setup>
import { onMounted, computed } from 'vue'
import { useStore } from 'vuex'

const store = useStore()
const { state, dispatch } = store

const user = computed(() => state.user)
const dailyGoals = computed(() => state.dailyGoals)

const hasDailyGoals = computed(() => dailyGoals.value.length > 0)
const totalConsumption = computed(() => hasDailyGoals.value ? dailyGoals.value[0].total_consumption : 0)

const remainingGoal = computed(() => {
  const remaining = user.value.daily_goal - totalConsumption.value
  return remaining > 0 ? remaining : 'você já bateu a meta do dia'
})
const consumptionPercentage = computed(() => ((totalConsumption.value / user.value.daily_goal) * 100).toFixed(2))

const goalStatusMessage = computed(() => hasDailyGoals.value && dailyGoals.value[0].goal_achieved
  ? 'Parabéns!! você já bateu a meta do dia'
  : 'Você ainda não bateu a meta hoje')


const fetchDailyGoals = async () => {
  try {
    if (user.value && user.value.id) {
      await dispatch('fetchDailyGoals')
    } else {
      console.error('Usuário não definido ou não possui ID')
    }
  } catch (error) {
    console.error('Erro ao buscar as metas diárias:', error)
  }
}

onMounted(fetchDailyGoals)
</script>
