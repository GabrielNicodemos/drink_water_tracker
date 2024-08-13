import { createStore } from 'vuex'
import axios from 'axios'

const store = createStore({
  state() {
    return {
      user: null,
      dailyGoals: {},
      historyGoals: [],
    }
  },
  mutations: {
    setUser(state, user) {
      state.user = user
    },
    setDailyGoals(state, goals) {
      state.dailyGoals = goals
    },
    setHistoryGoals(state, goals) {
      state.historyGoals = goals
    },
  },
  actions: {
    async login({ commit }, userData) {
      const response = await axios.post('/api/users/', userData)
      commit('setUser', response.data)
      return response.data
    },
    async fetchDailyGoals({ commit, state }) {
        try {
          const response = await axios.get(`/api/daily_goals/${state.user.id}/today`)
          commit('setDailyGoals', response.data)
        } catch (error) {
          console.error('Error fetching daily goals:', error)
        }
    },

    async fetchHistoryGoals({ commit, state }) {
      try {
        const response = await axios.get(`/api/daily_goals/${state.user.id}/history`)
        commit('setHistoryGoals', response.data)
      } catch (error) {
        console.error('Error fetching daily goals:', error)
      }
    },
  }
})

export default store
