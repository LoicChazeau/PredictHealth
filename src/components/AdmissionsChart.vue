<template>
  <v-card class="chart-card">
    <h3 class="chart-title">Évolution des Admissions</h3>
    <div ref="chart" class="chart-container"></div>
  </v-card>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import * as echarts from 'echarts'

const chart = ref(null)

onMounted(() => {
  const myChart = echarts.init(chart.value)

  const options = {
    tooltip: {
      trigger: 'axis',
      backgroundColor: '#fff',
      borderColor: '#ddd',
      borderWidth: 1,
      textStyle: { color: '#333' },
      axisPointer: { type: 'line', lineStyle: { color: '#888' } }
    },
    xAxis: {
      type: 'category',
      data: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
      axisLine: { lineStyle: { color: '#ccc' } },
      axisTick: { show: false },
      axisLabel: { color: '#666', fontSize: 12 }
    },
    yAxis: {
      type: 'value',
      axisLine: { show: false },
      splitLine: { lineStyle: { color: '#eee' } },
      axisLabel: { color: '#666', fontSize: 12 }
    },
    series: [
      {
        name: 'Admissions',
        type: 'line',
        smooth: true,
        showSymbol: true,
        symbol: 'circle',
        symbolSize: 8,
        itemStyle: { color: '#1c2440' },
        lineStyle: { width: 3, color: '#1c2440' },
        emphasis: {
          itemStyle: { color: '#ff6b6b' }
        },
        data: [8000, 8500, 9000, 9500, 10000, 10500, 11000, 10800, 10700, 10900, 11100, 11500]
      }
    ]
  }

  myChart.setOption(options)

  window.addEventListener('resize', () => {
    myChart.resize()
  })
})
</script>

<style scoped>
.chart-card {
  padding: 16px;
  border-radius: 12px;
  background-color: white;
  box-shadow: 0 5px 12px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.chart-title {
  font-size: 1.2rem;
  font-weight: bold;
  color: #1c2440;
  margin-bottom: 10px;
}

.chart-container {
  width: 100%;
  height: 300px;
}
</style>
