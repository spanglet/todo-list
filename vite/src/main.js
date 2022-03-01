import { createApp } from 'vue'
import App from './App.vue'
import { library } from "@fortawesome/fontawesome-svg-core"

// Icon imports from fontawesome
import { faPlus } from '@fortawesome/free-solid-svg-icons'
import { faMinus } from '@fortawesome/free-solid-svg-icons'
import { faCheck } from '@fortawesome/free-solid-svg-icons'
import { faXmark } from '@fortawesome/free-solid-svg-icons'

import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

// Icons are added for use in vue app
library.add(faPlus)
library.add(faMinus)
library.add(faCheck)
library.add(faXmark)

const hostname = '0.0.0.0';

app = createApp(App)
	.component("font-awesome-icon", FontAwesomeIcon) //fontawesome
	.mount('#app')
