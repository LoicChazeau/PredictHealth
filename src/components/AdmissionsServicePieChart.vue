<template>
    <v-card class="graph-card">
      <v-card-title>Répartition des Admissions par Service</v-card-title>
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
    if (props.filters.year) {
      params.date_debut = `${props.filters.year}-01-01`
      params.date_fin = `${props.filters.year}-12-31`
    }
    const response = await axios.get('http://localhost:8000/admissions/repartition', { params })
  
    const services = Object.keys(response.data)
    const values = Object.values(response.data)
  
    chartOptions.value = {
      tooltip: { trigger: 'item' },
      series: [{
        type: 'pie',
        radius: '50%',
        data: services.map((s, index) => ({
          name: s,
          value: values[index]
        }))
      }]
    }
  }
  
  watch(() => props.filters, fetchData, { deep: true })
  onMounted(fetchData)
  </script>
  