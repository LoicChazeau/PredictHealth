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
            <p class="card-title">Admissions Totales</p>
            <p class="card-subtitle">NB. total d'admissions</p>
          </v-col>
        </v-row>
        <v-row align="center">
          <v-col cols="6">
            <h2 class="stat-value">110,000</h2>
            <p class="card-footer">Cette année</p>
          </v-col>
          <v-col cols="6" class="d-flex align-center justify-end">
            <v-icon color="green">mdi-trending-up</v-icon>
            <span class="stat-change positive">3.9%</span>
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
            <p class="card-title">Occupation des Lits</p>
            <p class="card-subtitle">Pourcentage</p>
          </v-col>
        </v-row>
        <v-row align="center">
          <v-col cols="6">
            <h2 class="stat-value">85%</h2>
            <p class="card-footer">sur 1800 lits</p>
          </v-col>
          <v-col cols="6" class="d-flex align-center justify-end">
            <v-icon color="red">mdi-trending-down</v-icon>
            <span class="stat-change negative">0.7%</span>
          </v-col>
        </v-row>
      </v-card>
    </v-col>

    <v-col cols="12" md="4">
      <v-card class="stat-card">
        <v-row align="center">
          <v-col cols="2">
            <v-avatar size="34" color="grey-lighten-3">
              <v-icon size="26" color="black">mdi-account-off</v-icon>
            </v-avatar>
          </v-col>
          <v-col cols="10">
            <p class="card-title">Déficit de personnel</p>
            <p class="card-subtitle">par rapport aux besoins</p>
          </v-col>
        </v-row>
        <v-row align="center">
          <v-col cols="6">
            <h2 class="stat-value">12%</h2>
            <p class="card-footer">Aujourd'hui</p>
          </v-col>
          <v-col cols="6" class="d-flex align-center justify-end">
            <v-icon color="red">mdi-trending-down</v-icon>
            <span class="stat-change negative">0.7%</span>
          </v-col>
        </v-row>
      </v-card>
    </v-col>
  </v-row>
</template>

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
</style>
