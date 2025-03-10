<template>
  <div class="dashboard">
    <!-- Sidebar -->
    <Sidebar />

    <!-- Main Content Area -->
    <div class="main-content">
      <!-- Header -->
      <Header />

      <!-- Page Content -->
      <main class="page-content">
        <router-view />
      </main>
    </div>
  </div>
</template>

<script setup>
import Sidebar from './components/Sidebar.vue'
import Header from './components/Header.vue'
</script>

<style scoped>
.dashboard {
  display: flex;
  min-height: 100vh;
}

.main-content {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.page-content {
  padding: 20px;
  background: #333B6A;
  flex: 1;
}
</style>
