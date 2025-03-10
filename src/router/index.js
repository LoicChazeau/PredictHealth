import { createRouter, createWebHistory } from 'vue-router'

// Import des pages
import Home from '../views/Home.vue'
import Admissions from '../views/Admissions.vue'
import Previsions from '../views/Previsions.vue'
import Recommandations from '../views/Recommandations.vue'
import Parametres from '../views/Parametres.vue'


// Configuration des routes
const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/admissions', name: 'Admissions', component: Admissions },
  { path: '/previsions', name: 'Previsions', component: Previsions },
  { path: '/recommandations', name: 'Recommandations', component: Recommandations },
  { path: '/parametres', name: 'Parametres', component: Parametres }
]

// Création du router
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router
