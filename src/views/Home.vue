<template>
  <v-container fluid>
    <StatsCards />
    <v-row class="equal-height" align="stretch">
      <v-col cols="12" md="8">
        <AdmissionsChart class="full-height" />
      </v-col>
      <v-col cols="12" md="4">
        <AdmissionsComparison class="full-height" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import StatsCards from "../components/StatsCards.vue"
import AdmissionsChart from "../components/AdmissionsChart.vue"
import AdmissionsComparison from "../components/AdmissionsComparison.vue"
</script>

<style scoped>
.equal-height {
  display: flex;
}

.full-height {
  height: 100%;
}
</style>
