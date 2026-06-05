// src/router/index.ts

import { createRouter, createWebHistory } from 'vue-router'

import HomePage from '../pages/HomePage.vue'
import FlasherPage from '../pages/FlasherPage.vue'
import InfoPage from '../pages/InfoPage.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomePage,
    },
    {
      path: '/beta',
      name: 'beta-flasher',
      component: FlasherPage,
    },
    {
      path: '/info',
      name: 'info',
      component: InfoPage,
    },
  ],
})

export default router
