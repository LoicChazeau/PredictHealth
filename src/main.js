import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router'
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import '@mdi/font/css/materialdesignicons.css'
import { library } from "@fortawesome/fontawesome-svg-core";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { faHospital, faClock, faUserInjured, faCalendar } from "@fortawesome/free-solid-svg-icons";
import VueECharts from 'vue-echarts'


const vuetify = createVuetify({
    components,
    directives,
    icons: {
        defaultSet: 'mdi', 
      },
})

library.add(faHospital, faClock, faUserInjured, faCalendar);

const app = createApp(App)
app.component('v-chart', VueECharts)
app.component("font-awesome-icon", FontAwesomeIcon);
app.use(router)
app.use(vuetify)
app.mount('#app')
