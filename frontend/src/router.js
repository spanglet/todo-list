import * as VueRouter from 'vue-router'

import App from './App.vue'
import Login from './Login.vue'
import Registration from './Registration.vue'

// Page routes to feed into Vue-Router for SPA navigation
const routes = [
  { path: '/login', component: Login },
  { path: '/register', component: Registration },
  { path: '/app', component: App },
  { path: '/', component: App }
]

//Vue Router options for url routing
const router = VueRouter.createRouter({
  history: VueRouter.createWebHistory(),
  routes,
})

export {router}
