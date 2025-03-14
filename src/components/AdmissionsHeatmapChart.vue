<template>
    <v-card class="graph-card">
      <v-card-title>Heatmap Admissions Jour / Heure</v-card-title>
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
  try {
    const params = {}
    if (props.filters.year) params.year = props.filters.year

    const response = await axios.get('http://localhost:8000/heatmap/admissions', { params })

    chartOptions.value = {
      tooltip: { position: 'top' },
      grid: { height: '50%', top: '10%' },
      xAxis: {
        type: 'category',
        data: ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
      },
      yAxis: {
        type: 'category',
        data: ['0-4h', '4-8h', '8-12h', '12-16h', '16-20h', '20-24h']
      },
      visualMap: {
        min: 0,
        max: 100,
        calculable: true,
        orient: 'horizontal',
        left: 'center'
      },
      series: [{
        name: 'Admissions',
        type: 'heatmap',
        data: response.data.data
      }]
    }
  } catch (error) {
    console.error('Erreur API heatmap :', error)
  }
}

  
  watch(() => props.filters, fetchData, { deep: true })
  onMounted(fetchData)
  </script>
  