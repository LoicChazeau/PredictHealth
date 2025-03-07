<template>
    <div class="admissions-container">
      <div class="filters">
        <div class="filter-item" :class="{ active: selectedService }">
          <font-awesome-icon icon="hospital" class="filter-icon" />
          <select v-model="selectedService">
            <option value="">Sélectionner un Service</option>
            <option value="urgences">Urgences</option>
            <option value="cardiologie">Cardiologie</option>
            <option value="neurologie">Neurologie</option>
          </select>
        </div>
  
        <div class="filter-item" :class="{ active: selectedPeriod }">
          <font-awesome-icon icon="clock" class="filter-icon" />
          <select v-model="selectedPeriod">
            <option value=""> Périodes</option>
            <option value="matin">Matin</option>
            <option value="après-midi">Après-midi</option>
            <option value="soir">Soir</option>
          </select>
        </div>
  
        <div class="filter-item" :class="{ active: selectedPatientType }">
          <font-awesome-icon icon="user-injured" class="filter-icon" />
          <select v-model="selectedPatientType">
            <option value="">Type de patient</option>
            <option value="hospitalisé">Hospitalisé</option>
            <option value="ambulatoire">Ambulatoire</option>
          </select>
        </div>
      </div>
  
      <!-- ✅ Disposition en GRID -->
      <div class="grid-container">
        <div class="grid-row half-row">
          <ServiceChart class="grid-item half" />
          <OccupationChart class="grid-item half" />
        </div>
  
        <div class="grid-row two-thirds-row">
          <AdmissionsChart class="grid-item big" />
          <AdmissionsComparisonChart class="grid-item small" />
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { ref } from "vue";
  import { library } from "@fortawesome/fontawesome-svg-core";
  import { faHospital, faClock, faUserInjured } from "@fortawesome/free-solid-svg-icons";
  import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
  import ServiceChart from "../components/ServiceChart.vue";
  import OccupationChart from "../components/OccupationChart.vue";
  import AdmissionsChart from "../components/AdmissionsChart.vue";
  import AdmissionsComparisonChart from "../components/AdmissionsComparison.vue";
  
  library.add(faHospital, faClock, faUserInjured);
  
  export default {
    components: {
      ServiceChart,
      OccupationChart,
      AdmissionsChart,
      AdmissionsComparisonChart,
      FontAwesomeIcon
    },
    setup() {
      const selectedService = ref("");
      const selectedPeriod = ref("");
      const selectedPatientType = ref("");
  
      return { selectedService, selectedPeriod, selectedPatientType };
    }
  };
  </script>
  
  <style scoped>
 
  .admissions-container {
    padding: 20px;
    min-height: 100vh;
    overflow-y: auto;
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
  
  /* ✅ Active State */
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
  
  .full-width {
    width: 100%;
  }
  
  .half {
    width: 100%;
    height: 400px;
  }
  
  .big {
    width: 100%;
    height: 400px;
  }
  
  .small {
    width: 100%;
    height: 400px;
  }
  

  .chart {
    width: 100%;
    height: 100%;
  }
  </style>
  