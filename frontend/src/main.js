import { createApp } from 'vue'
import * as VueRouter from 'vue-router'
import App from './App.vue'
import Wrapper from './App.vue'
import Login from './Login.vue'
import { library } from "@fortawesome/fontawesome-svg-core"

// Icon imports from fontawesome
import { faPlus } from '@fortawesome/free-solid-svg-icons'
import { faMinus } from '@fortawesome/free-solid-svg-icons'
import { faCheck } from '@fortawesome/free-solid-svg-icons'
import { faXmark } from '@fortawesome/free-solid-svg-icons'
import { faAngleDown,faAngleUp } from '@fortawesome/free-solid-svg-icons'

import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

// Icons are added for use in vue app
library.add(faPlus)
library.add(faMinus)
library.add(faCheck)
library.add(faXmark)
library.add(faAngleDown)
library.add(faAngleUp)

const hostname = '0.0.0.0';

// page routes to feed into Vue-Router
const routes = [
  { path: '/login', component: Login },
  { path: '/', component: App }
]

//Vue Router options for url routing
const router = VueRouter.createRouter({
  history: VueRouter.createWebHistory(),
  routes,
})

const app = createApp(Wrapper)
	.component("font-awesome-icon", FontAwesomeIcon) //fontawesome
	.use(router)
	.mount('#app')

// Temporarily required to makeinjections automatically unwrap computed refs
// Will be unnecessary by Vue 3.3
app.config.unwrapInjectedRef = true
