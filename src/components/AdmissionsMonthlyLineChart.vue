<template>
    <v-card class="graph-card">
      <v-card-title>Évolution Mensuelle des Admissions</v-card-title>
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
  
    const response = await axios.get('http://localhost:8000/admissions/evolution', { params })
  
    const months = response.data.map(item => `Mois ${item.month}`)
    const admissions = response.data.map(item => item.admissions)
  
    chartOptions.value = {
      tooltip: { trigger: 'axis' },
      xAxis: { type: 'category', data: months },
      yAxis: { type: 'value' },
      series: [{
        data: admissions,
        type: 'line',
        smooth: true,
        areaStyle: {},
        lineStyle: { width: 3 }
      }]
    }
  }
  
  watch(() => props.filters, fetchData, { deep: true })
  onMounted(fetchData)
  </script>
  