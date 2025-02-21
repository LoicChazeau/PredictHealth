<template>
  <div>
    <nav>
      <ul>
        <li><router-link to="/">Accueil</router-link></li>
        <li><router-link to="/admissions">Admissions</router-link></li>
        <li><router-link to="/previsions">Prévisions</router-link></li>
        <li><router-link to="/recommandations">Recommandations</router-link></li>
      </ul>
    </nav>

    <router-view />
  </div>
</template>

<script setup>
</script>

<style>
nav ul {
  display: flex;
  gap: 20px;
  list-style-type: none;
  padding: 10px;
  background: #f4f4f9;
  border-bottom: 1px solid #ccc;
}

nav ul li {
  display: inline;
}

nav ul li a {
  text-decoration: none;
  color: #007bff;
  font-weight: bold;
}

nav ul li a:hover {
  color: #0056b3;
}
</style>
