<template>
    <div class="card">
      <h2>📅 Occupation par Jour</h2>
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
        xAxis: { type: "category", data: ["Lun", "Mar", "Mer", "Jeu", "Ven", "Sam", "Dim"] },
        yAxis: { type: "value" },
        series: [
          {
            name: "Occupation",
            type: "bar",
            data: [80, 60, 75, 90, 50, 95, 70],
            itemStyle: { color: "#00B0FF" },
            animationDuration: 1500
          }
        ]
      }));
      return { chartOptions };
    }
  });
  </script>
  