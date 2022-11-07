import { createApp, markRaw } from 'vue'
	
import { router } from './router.js'
import { axios } from "./axios.js"
import { createPinia } from 'pinia'
import Wrapper from './Wrapper.vue'


// Icon imports - Font Awesome
import { library } from "@fortawesome/fontawesome-svg-core"
import { faPlus,faMinus,faCheck,faXmark,
	faAngleDown,faAngleUp} from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome"

// Icon registration
library.add(faPlus,faMinus,faCheck,faXmark,
	faAngleDown,faAngleUp)

const pinia = createPinia()
// router added globally to Pinia stores
pinia.use(({ store }) => {
  store.router = markRaw(router)
})

const app = createApp(Wrapper)
	.component("font-awesome-icon", FontAwesomeIcon) 
	.use(router)
  	.use(pinia)

app.config.globalProperties.axios = axios
app.config
app.mount('#app')

// Temporarily required to make injections automatically unwrap computed refs
// Will be unnecessary by Vue 3.3
app.config.unwrapInjectedRef = true

