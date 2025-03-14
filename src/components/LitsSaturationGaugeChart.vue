<template>
    <v-card class="graph-card">
      <v-card-title>Taux d'Occupation des Lits</v-card-title>
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
    const response = await axios.get('http://localhost:8000/dashboard', { params })
  
    const tauxOccupation = parseFloat(response.data.taux_occupation.replace('%', ''))
  
    chartOptions.value = {
      series: [{
        type: 'gauge',
        startAngle: 180,
        endAngle: 0,
        center: ['50%', '75%'],
        radius: '90%',
        min: 0,
        max: 100,
        axisLine: { lineStyle: { width: 20 } },
        pointer: { icon: 'rect', length: '60%', width: 8 },
        detail: { valueAnimation: true, formatter: '{value}%', fontSize: 24 },
        data: [{ value: tauxOccupation, name: 'Occupation' }]
      }]
    }
  }
  
  watch(() => props.filters, fetchData, { deep: true })
  onMounted(fetchData)
  </script>
  