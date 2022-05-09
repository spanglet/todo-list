
import * as VueRouter from 'vue-router'

// Page routes to feed into Vue-Router for SPA navigation
const routes = [
  { path: '/login', component: Login },
  { path: '/register', component: Registration },
  { path: '/app', component: App }
]

//Vue Router options for url routing
const router = VueRouter.createRouter({
  history: VueRouter.createWebHistory(),
  routes,
})


export {router}
