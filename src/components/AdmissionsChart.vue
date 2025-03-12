<template>
  <v-card class="chart-card">
    <h3 class="chart-title">Évolution des admissions sur {{ year }}</h3>
    <div ref="chart" class="chart-container"></div>
  </v-card>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import axios from 'axios'
import * as echarts from 'echarts'

const chart = ref(null)
const admissionsData = ref([])
const monthsLabels = ref(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
const year = ref(null)

const fetchData = async () => {
  try {
    const response = await axios.get('http://localhost:8000/evolution-admissions')
    admissionsData.value = response.data.admissions
    year.value = response.data.annee
  } catch (error) {
    console.error('Erreur lors de la récupération des données du graphique :', error)
  }
}

onMounted(async () => {
  await fetchData()

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
      data: monthsLabels.value,
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
        data: admissionsData.value
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
