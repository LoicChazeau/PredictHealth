<template>
    <div class="card">
      <h2>📊 Répartition par Service</h2>
      <v-chart class="chart" :option="chartOptions" autoresize />
    </div>
  </template>
  
  <script>
  import { defineComponent, computed } from "vue";
  import VChart from "vue-echarts";
  
  export default defineComponent({
    components: { VChart },
    setup() {
      const chartOptions = computed(() => ({
        tooltip: { trigger: "item" },
        series: [
          {
            name: "Services",
            type: "pie",
            radius: "50%",
            data: [
              { value: 50, name: "Urgences" },
              { value: 20, name: "Cardiologie" },
              { value: 10, name: "Neurologie" },
            ],
            animationDuration: 2000
          }
        ]
      }));
      return { chartOptions };
    }
  });
  </script>
  
  <style scoped>
  .chart {
    width: 100%;
    height: 300px;
  }
  </style>
  