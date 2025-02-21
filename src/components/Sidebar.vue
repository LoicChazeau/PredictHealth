<template>
    <aside class="sidebar">
        <div class="logo">
            <img src="../assets/logo.png" alt="PredictHealth" class="logo-img">
        </div>
        <ul>
            <li>
                <router-link to="/">
                    <span>🏠</span> Accueil
                </router-link>
            </li>
            <li>
                <router-link to="/admissions">
                    <span>📊</span> Admissions
                </router-link>
            </li>
            <li>
                <router-link to="/previsions">
                    <span>📈</span> Prévisions
                </router-link>
            </li>
            <li>
                <router-link to="/recommandations">
                    <span>💡</span> Recommandations
                </router-link>
            </li>
        </ul>
    </aside>
</template>

<script setup>
</script>

<style scoped>
.sidebar {
    width: 240px;
    background: #fff;
    box-shadow: 2px 0 4px rgba(0, 0, 0, 0.1);
    padding: 20px;
}

.sidebar ul {
    list-style: none;
    padding: 0;
}

.sidebar ul li {
    margin: 20px 0;
}

.sidebar ul li a {
    text-decoration: none;
    color: #4f46e5;
    font-weight: bold;
    display: flex;
    align-items: center;
}

.sidebar ul li a span {
    margin-right: 10px;
}

.logo {
    margin-top: 0px;
    margin-bottom: 70px;
}

.logo-img {
    width: 90%;
}
</style>