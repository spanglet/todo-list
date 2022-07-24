import * as VueRouter from 'vue-router'
import { axios } from "./axios.js"

import App from './App.vue'
import Login from './Login.vue'
import Registration from './Registration.vue'
import Wrapper from './Wrapper.vue'
import Calendar from './components/Calendar.vue'
import TodoList from './components/TodoList.vue'

// Page routes to feed into Vue-Router for SPA navigation
const routes = [
  { path: '/login', component: Login },
  { path: '/register', component: Registration },
  { path: '/app',
    component: App,
    children: [
      // Children are rendered inside App's <router-view>
      {
        path: 'calendar/:calView',
        name: 'calendar',
        component: Calendar,
        props: true
      },
      {
        path: 'todo/:id',
        name: 'todo',
        component: TodoList,
        props: true,
      },
    ]
  },
  { path: '/', component: Wrapper },
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
