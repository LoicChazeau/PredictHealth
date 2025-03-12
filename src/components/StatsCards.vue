<template>
  <v-row class="stats-container">
    <v-col cols="12" md="4">
      <v-card class="stat-card">
        <v-row align="center">
          <v-col cols="2">
            <v-avatar size="34" color="grey-lighten-3">
              <v-icon size="26" color="black">mdi-account-group</v-icon>
            </v-avatar>
          </v-col>
          <v-col cols="10">
            <p class="card-title">Admissions totales</p>
          </v-col>
        </v-row>
        <v-row align="center">
          <v-col cols="6">
            <h2 class="stat-value">{{ stats.admissions_jour }}</h2>
            <p class="card-footer">Aujourd'hui</p>
          </v-col>
          <v-col cols="6" class="d-flex align-center justify-end">
            <v-icon :color="getTrendColor(stats.evolution_admissions)">
              {{ getTrendIcon(stats.evolution_admissions) }}
            </v-icon>
            <span :class="getTrendClass(stats.evolution_admissions)">
              {{ Math.abs(parseFloat(stats.evolution_admissions)) }}%
            </span>
          </v-col>
        </v-row>
      </v-card>
    </v-col>

    <v-col cols="12" md="4">
      <v-card class="stat-card">
        <v-row align="center">
          <v-col cols="2">
            <v-avatar size="34" color="grey-lighten-3">
              <v-icon size="26" color="black">mdi-bed</v-icon>
            </v-avatar>
          </v-col>
          <v-col cols="10">
            <p class="card-title">Occupation des lits</p>
          </v-col>
        </v-row>
        <v-row align="center">
          <v-col cols="6">
            <h2 class="stat-value">{{ stats.taux_occupation }}</h2>
            <p class="card-footer">Actuellement</p>
          </v-col>
          <v-col cols="6" class="d-flex align-center justify-end">
            <v-icon :color="getTrendColor(stats.evolution_taux_occupation)">
              {{ getTrendIcon(stats.evolution_taux_occupation) }}
            </v-icon>
            <span :class="getTrendClass(stats.evolution_taux_occupation)">
              {{ Math.abs(parseFloat(stats.evolution_taux_occupation)) }}
            </span>
          </v-col>
        </v-row>
      </v-card>
    </v-col>

    <v-col cols="12" md="4">
      <v-card class="stat-card">
        <v-row align="center">
          <v-col cols="2">
            <v-avatar size="34" color="grey-lighten-3">
              <v-icon size="26" color="black">mdi-clock-outline</v-icon>
            </v-avatar>
          </v-col>
          <v-col cols="10">
            <p class="card-title">Temps d'attente moyen</p>
          </v-col>
        </v-row>
        <v-row align="center">
          <v-col cols="6">
            <h2 class="stat-value">{{ stats.temps_attente_jour }}</h2>
            <p class="card-footer">Actuellement</p>
          </v-col>
          <v-col cols="6" class="d-flex align-center justify-end">
            <v-icon :color="getTrendColor(stats.evolution_temps_attente)">
              {{ getTrendIcon(stats.evolution_temps_attente) }}
            </v-icon>
            <span :class="getTrendClass(stats.evolution_temps_attente)">
              {{ Math.abs(parseFloat(stats.evolution_temps_attente)) }}
            </span>
          </v-col>
        </v-row>
      </v-card>
    </v-col>
  </v-row>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";

const stats = ref({
  admissions_jour: "-",
  evolution_admissions: "-",
  taux_occupation: "-",
  evolution_taux_occupation: "-",
  temps_attente_jour: "-",
  evolution_temps_attente: "-",
});

const fetchStats = async () => {
  try {
    const response = await axios.get("http://localhost:8000/dashboard");
    stats.value = response.data;
  } catch (error) {
    console.error("Erreur lors de la récupération des stats :", error);
  }
};

// Déclencher l'appel API au montage du composant
onMounted(fetchStats);

// Déterminer la classe et l'icône en fonction de l'évolution
const getTrendClass = (value) => {
  return parseFloat(value) > 0 ? "negative" : "positive";
};

const getTrendColor = (value) => {
  return parseFloat(value) > 0 ? "red" : "green";
};

const getTrendIcon = (value) => {
  return parseFloat(value) > 0 ? "mdi-trending-down" : "mdi-trending-up";
};
</script>

<style scoped>
.stats-container {
  display: flex;
  justify-content: space-between;
}

.stat-card {
  padding: 16px;
  border-radius: 12px;
  background-color: white;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease-in-out;
}

.stat-card:hover {
  transform: scale(1.03);
}

.card-title {
  font-size: 1rem;
  font-weight: bold;
  color: #1c2440;
}

.card-subtitle {
  font-size: 0.85rem;
  color: gray;
}

.stat-value {
  font-size: 2rem;
  font-weight: bold;
  color: #212121;
}

.card-footer {
  font-size: 0.85rem;
  color: gray;
}

.stat-change {
  font-size: 1rem;
  font-weight: bold;
  margin-left: 5px;
}

.stat-change.positive {
  color: green;
}

.stat-change.negative {
  color: red;
}

.negative {
  color: red;
  font-weight: 600;
  padding-left: 5px
}

.positive {
  color: green;
  font-weight: 600;
  padding-left: 5px
}
</style>
