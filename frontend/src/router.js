import * as VueRouter from 'vue-router'
import { axios } from "./axios.js"

import App from './App.vue'
import Login from './Login.vue'
import Registration from './Registration.vue'
import Wrapper from './Wrapper.vue'

// Page routes to feed into Vue-Router for SPA navigation
const routes = [
  { path: '/login', component: Login },
  { path: '/register', component: Registration },
  { path: '/app', component: App },
  { path: '/', component: Wrapper }
]

//Vue Router options for url routing
const router = VueRouter.createRouter({
  history: VueRouter.createWebHistory(),
  routes,
})

router.beforeEach((to, from) => {
  if (to.path == "/logout") {
    axios.get("/auth/logout")
    return {path: "/login"}
  }
})

export {router}
