import { createApp } from 'vue'

import { router } from './router.js'
import Wrapper from './Wrapper.vue'

// Icon imports
import { library } from "@fortawesome/fontawesome-svg-core"
import { faPlus,faMinus,faCheck,faXmark,
	faAngleDown,faAngleUp} from '@fortawesome/free-solid-svg-icons'

import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

// Icon registration
library.add(faPlus,faMinus,faCheck,faXmark,
	faAngleDown,faAngleUp)


const app = createApp(Wrapper)
	.component("font-awesome-icon", FontAwesomeIcon) 
	.use(router)

app.mount('#app')

axios.defaults.baseURL = 'http://127.0.0.1:5000/';
axios.defaults.headers.post['Content-Type'] = "application/json"
axios.defaults.headers.common['Access-Control-Allow-Origin'] = 'http://127.0.0.1:5000/'
axios.defaults.withCredentials = true

// Temporarily required to makeinjections automatically unwrap computed refs
// Will be unnecessary by Vue 3.3
app.config.unwrapInjectedRef = true

