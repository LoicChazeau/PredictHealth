<template>
  <div class="admissions-container">
    <!-- Filtres -->
    <div class="filters">
      <!-- Filtre Service -->
      <div class="filter-item" :class="{ active: selectedService }">
        <font-awesome-icon icon="hospital" class="filter-icon" />
        <select v-model="selectedService">
          <option value="">Tous les services</option>
          <option v-for="service in services" :key="service" :value="service">
            {{ service }}
          </option>
        </select>
      </div>

      <!-- Filtre Année -->
      <div class="filter-item" :class="{ active: selectedYear }">
        <!-- Icône calendrier -->
        <font-awesome-icon icon="calendar" class="filter-icon" />
        <select v-model="selectedYear">
          <option value="">Toutes les années</option>
          <option v-for="year in years" :key="year" :value="year">
            {{ year }}
          </option>
        </select>
      </div>
    </div>

    <!-- Contenu dynamique : transmission des filtres aux composants -->
    <div class="grid-container">
      <div class="grid-row half-row">
        <AdmissionsChart :filters="currentFilters" class="grid-item big" />
        <AdmissionsComparisonChart :filters="currentFilters" class="grid-item small" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from "vue";
import axios from "axios";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import AdmissionsChart from "../components/AdmissionsChart.vue";
import AdmissionsComparisonChart from "../components/AdmissionsComparisonChart.vue";

// Filtres réactifs
const selectedService = ref("");
const selectedYear = ref("");
const services = ref([]);

// Liste d'années
const years = ref(["2020", "2021", "2022", "2023", "2024"]);

// Récupérer la liste des services depuis l'API /filters (si disponible)
const fetchFilters = async () => {
  try {
    const response = await axios.get("http://localhost:8000/filters");
    services.value = response.data.services;
  } catch (error) {
    console.error("Erreur lors de la récupération des filtres :", error);
    // Valeurs par défaut en cas d'erreur
    services.value = ["Neurologie", "Psychiatrie", "Gériatrie", "Soins intensifs", "Chirurgie", "Cardiologie", "Urgences"];
  }
};

onMounted(() => {
  fetchFilters();
});

// Objet regroupant les filtres sélectionnés
const currentFilters = computed(() => ({
  service: selectedService.value,
  year: selectedYear.value
}));

// Observer les filtres
watch(currentFilters, (newFilters) => {
  console.log("Filtres mis à jour :", newFilters);
});
</script>

<style scoped>
.admissions-container {
  padding: 20px;
  min-height: 50vh;
  overflow-y: hidden;
}

.filters {
  display: flex;
  justify-content: center;
  gap: 15px;
  margin-bottom: 20px;
}

.filter-item {
  display: flex;
  align-items: center;
  gap: 10px;
  background: white;
  color: #1e1e2f;
  padding: 12px 20px;
  border-radius: 25px;
  border: 1px solid #ccc;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
  box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
}

.filter-item select {
  background: transparent;
  border: none;
  outline: none;
  font-size: 14px;
  cursor: pointer;
  color: #1e1e2f;
}

.filter-item:hover {
  background: #007bff;
  color: white;
  box-shadow: 2px 2px 10px rgba(0, 123, 255, 0.3);
}

.filter-item select:hover {
  color: white;
}

.filter-icon {
  font-size: 16px;
}

.filter-item.active {
  background: #007bff;
  color: white;
  border: none;
}

.grid-container {
  display: grid;
  gap: 20px;
  max-width: 1200px;
  margin: auto;
}

.half-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  width: 100%;
  align-items: stretch;
}

.two-thirds-row {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 20px;
  width: 100%;
  align-items: stretch;
}

.grid-item {
  background: white;
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 400px;
}
</style>
