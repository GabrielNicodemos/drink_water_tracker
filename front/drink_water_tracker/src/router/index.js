import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'
import HomeView from '../views/HomeView.vue'
import DrinkWaterHistory from '../views/DrinkWaterHistory.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
        path: '/',
        name: 'Login',
        component: Login
    },
    {
        path: '/home',
        name: 'Home',
        component: HomeView
    },
    {
        path: '/history',
        name: 'History',
        component: DrinkWaterHistory
    },
  ]
})

export default router
