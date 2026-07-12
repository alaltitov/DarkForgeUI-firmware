// src/main.ts

import { createApp } from 'vue'

import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'
import i18n from './plugins/i18n'
import yandexMetrika from 'yandex-metrika-vue3'

import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'

const app = createApp(App)

app.use(router)
app.use(vuetify)
app.use(i18n)

app.use(yandexMetrika, {
  id: 110625024,
  router: router,
  env: import.meta.env.MODE,
  options: {
    clickmap: true,
    trackLinks: true,
    accurateTrackBounce: true,
    webvisor: true
  }
})

app.mount('#app')
