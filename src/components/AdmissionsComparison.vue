<template>
  <v-card class="comparison-card">
    <h3 class="title">Admissions</h3>

    <div class="graph-container">
      <!-- Réalité -->
      <div class="column">
        <div class="bubble reality">
          <span>85%</span>
        </div>
        <div class="bar reality-bar"></div>
        <p class="label">Réalité</p>
      </div>

      <!-- Prévisions -->
      <div class="column">
        <div class="bubble prediction">
          <span>88%</span>
        </div>
        <div class="bar prediction-bar"></div>
        <p class="label">Prévisions</p>
      </div>
    </div>

    <!-- Légende -->
    <div class="legend">
      <div class="legend-item">
        <div class="legend-dot reality-dot"></div>
        <span>Réalité</span>
      </div>
      <div class="legend-item">
        <div class="legend-dot prediction-dot"></div>
        <span>Prévisions</span>
      </div>
    </div>
  </v-card>
</template>

<style scoped>
.comparison-card {
  padding: 20px;
  border-radius: 16px;
  background-color: white;
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
  text-align: center;
  width: 100%;
  max-width: 350px;
  margin: auto;
}

.title {
  font-size: 1.2rem;
  font-weight: bold;
  color: #1c2440;
  margin-bottom: 10px;
}

.graph-container {
  display: flex;
  justify-content: space-around;
  align-items: flex-end;
  height: 140px;
  padding: 10px 0;
  margin-top: 36px;
}

.column {
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  width: 50px;
}

.bubble {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1rem;
  font-weight: bold;
  color: white;
  position: absolute;
  top: -30px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.reality {
  background-color: #1c2440;
}

.prediction {
  background-color: #b0b0b0;
}

.bar {
  width: 10px;
  border-radius: 10px;
  transition: height 0.5s ease-in-out;
}

.reality-bar {
  height: 85px; /* 85% */
  background-color: #1c2440;
}

.prediction-bar {
  height: 88px; /* 88% */
  background-color: #b0b0b0;
}

.label {
  font-size: 0.9rem;
  font-weight: 500;
  color: #666;
  margin-top: 5px;
}

.legend {
  margin-top: 46px;
  display: flex;
  justify-content: center;
  gap: 20px;
}

.legend-item {
  display: flex;
  align-items: center;
  gap: 5px;
}

.legend-dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
}

.reality-dot {
  background-color: #1c2440;
}

.prediction-dot {
  background-color: #b0b0b0;
}
</style>
