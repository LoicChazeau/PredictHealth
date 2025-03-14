<template>
    <v-card class="graph-card">
      <v-card-title>Prédiction Admissions (7 jours)</v-card-title>
      <v-card-text>
        <v-chart :option="chartOptions" autoresize style="height: 400px;" />
      </v-card-text>
    </v-card>
  </template>
  
  <script setup>
  import { ref, watch, onMounted } from 'vue'
  import VChart from 'vue-echarts'
  import axios from 'axios'
  
  const props = defineProps({ filters: Object })
  const chartOptions = ref({})
  
  const fetchData = async () => {
    const params = {}
    if (props.filters.year) params.year = props.filters.year
    if (props.filters.service) params.service = props.filters.service
  
    const historyRes = await axios.get('http://localhost:8000/admissions/evolution', { params })
    const predictRes = await axios.get('http://localhost:8000/predict/2024-05-01') // exemple à changer selon date dynamique
  
    const months = historyRes.data.map(item => `Mois ${item.month}`)
    const admissions = historyRes.data.map(item => item.admissions)
  
    const predictions = [...admissions.slice(-1), predictRes.data.prediction, predictRes.data.prediction + 10, predictRes.data.prediction + 20]
  
    chartOptions.value = {
      tooltip: { trigger: 'axis' },
      legend: { data: ['Historique', 'Prédictions'] },
      xAxis: { type: 'category', data: [...months, 'Pred J+1', 'Pred J+2', 'Pred J+3'] },
      yAxis: { type: 'value' },
      series: [
        { name: 'Historique', type: 'line', data: admissions },
        { name: 'Prédictions', type: 'line', data: predictions, lineStyle: { type: 'dashed' } }
      ]
    }
  }
  
  watch(() => props.filters, fetchData, { deep: true })
  onMounted(fetchData)
  </script>
  