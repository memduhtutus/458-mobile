import './index.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { required, email, min } from '@vee-validate/rules'
import { defineRule } from 'vee-validate'
import Toast, { type PluginOptions } from 'vue-toastification'
import 'vue-toastification/dist/index.css'

import App from './App.vue'
import router from './router'

defineRule('required', required)
defineRule('email', email)
defineRule('min', min)

const app = createApp(App)

const options: PluginOptions = {
  transition: 'Vue-Toastification__fade',
  maxToasts: 20,
  timeout: 3000,
}

app.use(createPinia())
app.use(router)
app.use(Toast, options)

app.mount('#app')
