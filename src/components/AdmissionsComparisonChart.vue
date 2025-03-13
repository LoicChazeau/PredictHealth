<template>
    <v-card class="chart-card">
        <h3 class="chart-title">Répartition par jour de la semaine sur {{ yearDisplay }}</h3>
        <div ref="chart" class="chart-container"></div>
    </v-card>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import axios from 'axios'
import * as echarts from 'echarts'

// Recevoir les filtres depuis le composant parent
const props = defineProps({
    filters: {
        type: Object,
        default: () => ({})
    }
})

const chart = ref(null)
const distributionData = ref([])
const yearDisplay = ref("Toutes les années")

// Ordre des jours en français pour le tri
const dayOrder = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

const fetchDistribution = async () => {
    try {
        const params = {}
        if (props.filters.year && props.filters.year !== "") {
            params.year = props.filters.year
            yearDisplay.value = props.filters.year
        } else {
            yearDisplay.value = "Toutes les années"
        }
        if (props.filters.service && props.filters.service !== "") {
            params.service = props.filters.service
        }
        const response = await axios.get("http://localhost:8000/admissions/distribution", { params })
        let data = response.data; // Attendu: tableau d'objets { day: "Monday", admissions: X }

        // Table de correspondance des jours en anglais vers le français
        const dayMapping = {
            "Monday": "Lundi",
            "Tuesday": "Mardi",
            "Wednesday": "Mercredi",
            "Thursday": "Jeudi",
            "Friday": "Vendredi",
            "Saturday": "Samedi",
            "Sunday": "Dimanche"
        };

        // Convertir les jours en français et trier selon l'ordre français
        data = data.map(item => ({
            day: dayMapping[item.day] || item.day,
            admissions: item.admissions
        })).sort((a, b) => dayOrder.indexOf(a.day) - dayOrder.indexOf(b.day));

        distributionData.value = data;
    } catch (error) {
        console.error("Erreur lors de la récupération des données de répartition :", error)
    }
}

onMounted(() => {
    fetchDistribution();
});

// Si les filtres changent, recharger les données
watch(() => props.filters, () => {
    fetchDistribution();
}, { deep: true });

// Mettre à jour le graphique quand distributionData change
watch(distributionData, (newData) => {
    if (newData && chart.value) {
        const myChart = echarts.init(chart.value)
        const xData = newData.map(item => item.day)
        const yData = newData.map(item => item.admissions)

        const options = {
            tooltip: {
                trigger: 'axis',
                axisPointer: { type: 'shadow' }
            },
            xAxis: {
                type: 'category',
                data: xData,
                axisLine: { lineStyle: { color: '#ccc' } },
                axisTick: { alignWithLabel: true },
                axisLabel: { color: '#666', fontSize: 12 }
            },
            yAxis: {
                type: 'value',
                axisLine: { show: false },
                splitLine: { lineStyle: { color: '#eee' } },
                axisLabel: { color: '#666', fontSize: 12 }
            },
            series: [{
                name: 'Admissions',
                type: 'bar',
                data: yData,
                itemStyle: { color: '#1c2440' },
                barWidth: '50%'
            }]
        }
        myChart.setOption(options)
        window.addEventListener('resize', () => {
            myChart.resize()
        })
    }
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