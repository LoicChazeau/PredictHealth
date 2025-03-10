<template>
    <div>
        <h1>Prévisions</h1>
        <button @click="fetchData">Charger les données</button>
        <ul>
            <li v-for="(item, index) in data" :key="index">
                {{ item }}
            </li>
        </ul>
    </div>
</template>

<script setup>
import { ref } from "vue";
import { getData } from "../services/api";

const data = ref([]);

const fetchData = async () => {
    data.value = await getData();
};
</script>