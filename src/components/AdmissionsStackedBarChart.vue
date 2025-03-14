<template>
    <v-card class="graph-card">
      <v-card-title>Admissions par Service (Mois)</v-card-title>
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
  
  // Exemple de services
  const servicesList = ['Neurologie', 'Psychiatrie', 'Gériatrie', 'Chirurgie', 'Urgences']
  
  const fetchData = async () => {
    const params = {}
    if (props.filters.year) params.year = props.filters.year
  
    const seriesData = []
  
    for (const service of servicesList) {
      const response = await axios.get('http://localhost:8000/admissions/evolution', {
        params: { ...params, service }
      })
  
      const data = response.data.map(item => item.admissions)
  
      seriesData.push({
        name: service,
        type: 'bar',
        stack: 'total',
        emphasis: { focus: 'series' },
        data
      })
    }
  
    const months = ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Juin', 'Juil', 'Août', 'Sep', 'Oct', 'Nov', 'Déc']
  
    chartOptions.value = {
      tooltip: { trigger: 'axis' },
      legend: {},
      xAxis: { type: 'category', data: months },
      yAxis: { type: 'value' },
      series: seriesData
    }
  }
  
  watch(() => props.filters, fetchData, { deep: true })
  onMounted(fetchData)
  </script>
  