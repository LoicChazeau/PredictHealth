<template>
  <v-card class="chart-card">
    <h3>Évolution des Admissions</h3>
    <div ref="chart" class="chart-container"></div>
  </v-card>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import * as echarts from 'echarts'

const chart = ref(null)

onMounted(() => {
  const myChart = echarts.init(chart.value)
  myChart.setOption({
    xAxis: { type: 'category', data: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] },
    yAxis: { type: 'value' },
    series: [{ data: [8000, 9000, 9500, 10000, 10500, 11000, 11500, 10800, 11200, 12000], type: 'line' }]
  })
})
</script>

<style scoped>
.chart-card {
  padding: 16px;
  border-radius: 12px;
  background-color: white;
}

.chart-container {
  width: 100%;
  height: 250px;
}
</style>
