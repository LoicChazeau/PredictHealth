<template>
    <v-container class="admissions-container" fluid>
  
      <!-- FILTRES INLINE - ALIGNÉS & MODERNES -->
      <v-row
        justify="center"
        align="center"
        class="filters-row pa-4"
        style="gap: 20px;"
      >
        <!-- FILTRE SERVICE -->
        <v-btn
          class="filter-btn"
          color="primary"
          variant="flat"
          size="large"
          rounded="xl"
          @click="openServiceDialog = true"
        >
          <v-icon left>mdi-hospital-building</v-icon>
          {{ selectedService || 'Tous les services' }}
        </v-btn>
  
        <!-- FILTRE ANNÉE -->
        <v-btn
          class="filter-btn"
          color="primary"
          variant="flat"
          size="large"
          rounded="xl"
          @click="openYearDialog = true"
        >
          <v-icon left>mdi-calendar</v-icon>
          {{ selectedYear || 'Toutes les années' }}
        </v-btn>
  
        <!-- BOUTON RESET -->
        <v-btn
          class="reset-btn"
          color="red darken-1"
          size="large"
          variant="outlined"
          rounded="xl"
          @click="resetFilters"
        >
          <v-icon left>mdi-refresh</v-icon>
          Réinitialiser
        </v-btn>
      </v-row>
  
      <!-- DIALOG POUR LE FILTRE SERVICE -->
      <v-dialog v-model="openServiceDialog" max-width="400px">
        <v-card class="dialog-card">
          <v-card-title>Choisissez un service</v-card-title>
          <v-card-text>
            <v-select
              v-model="selectedService"
              :items="services"
              label="Services"
              clearable
              variant="solo"
              density="comfortable"
              color="primary"
            />
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn text @click="openServiceDialog = false">Fermer</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
  
      <!-- DIALOG POUR LE FILTRE ANNÉE -->
      <v-dialog v-model="openYearDialog" max-width="400px">
        <v-card class="dialog-card">
          <v-card-title>Choisissez une année</v-card-title>
          <v-card-text>
            <v-select
              v-model="selectedYear"
              :items="years"
              label="Années"
              clearable
              variant="solo"
              density="comfortable"
              color="primary"
            />
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn text @click="openYearDialog = false">Fermer</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
  
      <!-- CONTENU : GRAPHIQUES -->
      <v-row dense class="grid-container mt-10">
        <v-col cols="12" md="8">
          <AdmissionsChart :filters="currentFilters" class="grid-item" />
        </v-col>
        <v-col cols="12" md="4">
          <AdmissionsComparisonChart :filters="currentFilters" class="grid-item" />
        </v-col>
      </v-row>
    </v-container>
  </template>
<script setup>
import { ref, computed, onMounted, watch } from "vue"
import axios from "axios"
import AdmissionsChart from "../components/AdmissionsChart.vue"
import AdmissionsComparisonChart from "../components/AdmissionsComparisonChart.vue"

// Variables filtres
const selectedService = ref("")
const selectedYear = ref("")

// Booleans pour les dialogs
const openServiceDialog = ref(false)
const openYearDialog = ref(false)

// Données statiques
const services = ref([])
const years = ref(["2020", "2021", "2022", "2023", "2024"])

// Fetch Services depuis API
const fetchFilters = async () => {
  try {
    const response = await axios.get("http://localhost:8000/filters")
    services.value = response.data.services
  } catch (error) {
    console.error("Erreur de récupération des filtres :", error)
    services.value = ["Neurologie", "Psychiatrie", "Gériatrie", "Soins intensifs", "Chirurgie", "Cardiologie", "Urgences"]
  }
}

// Reset des filtres
const resetFilters = () => {
  selectedService.value = ""
  selectedYear.value = ""
}

onMounted(fetchFilters)

const currentFilters = computed(() => ({
  service: selectedService.value,
  year: selectedYear.value
}))

watch(currentFilters, (filters) => {
  console.log("Filtres actifs :", filters)
})
</script>
<style scoped>
.admissions-container {
  padding-top: 48px;
}

.filters-row {
  display: flex;
  justify-content: center;
  align-items: center;
}

.filter-btn,
.reset-btn {
  transition: 0.3s ease;
  text-transform: none;
  font-weight: 600;
  letter-spacing: 0.5px;
  box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.1);
}

.filter-btn:hover,
.reset-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0px 12px 25px rgba(0, 0, 0, 0.2);
}

.filter-btn {
  background: linear-gradient(90deg, #007bff, #0056b3);
  color: white;
}

.reset-btn {
  border-color: #ff6b6b;
  color: #ff6b6b;
}

.reset-btn:hover {
  background-color: #ff6b6b !important;
  color: white !important;
}

.dialog-card {
  border-radius: 16px;
  backdrop-filter: blur(10px);
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.2);
}

.grid-container {
  margin-top: 30px;
}

.grid-item {
  border-radius: 16px;
  padding: 20px;
  background: white;
  box-shadow: 0px 8px 30px rgba(0, 0, 0, 0.1);
}

@media (prefers-color-scheme: dark) {
  .grid-item {
    background-color: #1e1e1e;
  }
  .filter-btn {
    background: linear-gradient(90deg, #1e88e5, #1565c0);
  }
  .dialog-card {
    background: rgba(40, 40, 40, 0.8);
  }
}
</style>
