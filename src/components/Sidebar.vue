<template>
    <aside class="sidebar">
        <div class="logo">
            <img src="../assets/logo.png" alt="PredictHealth" class="logo-img">
        </div>
        <div class="sidebar-container">
            <div class="sidebar-content">
                <router-link to="/" class="sidebar-btn">
                    <img src="../assets/dashboard.svg" alt="Accueil">
                    <span>Accueil</span>
                </router-link>
                <router-link to="/admissions" class="sidebar-btn">
                    <img src="../assets/collections.svg" alt="Admissions">
                    <span>Admissions</span>
                </router-link>
                <router-link to="/previsions" class="sidebar-btn">
                    <img src="../assets/insert_invitation.svg" alt="Prévisions">
                    <span>Prévisions</span>
                </router-link>
                <router-link to="/recommandations" class="sidebar-btn">
                    <img src="../assets/thumb_up.svg" alt="Recommandations">
                    <span>Recommandations</span>
                </router-link>
                <router-link to="/parametres" class="sidebar-btn">
                    <img src="../assets/settings.svg" alt="Paramètres">
                    <span>Paramètres</span>
                </router-link>
            </div>
            <router-link to="/logout" class="sidebar-footer sidebar-btn">
                <img src="../assets/power_settings_new.svg" alt="Déconnexion">
                <span>Déconnexion</span>
            </router-link>
        </div>
    </aside>
</template>

<script setup>
</script>

<style scoped>
.sidebar {
    height: 100vh;
    background: #fff;
    box-shadow: 2px 0 4px rgba(0, 0, 0, 0.1);
    padding: 20px;
}

.sidebar-container {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: calc(100% - 110px);
}

.sidebar-content {
    display: flex;
    flex-direction: column;
}

.sidebar-btn {
    display: flex;
    align-items: center;
    padding: 10px 20px;
    margin-bottom: 35px;
    color: #333B6A;
    text-decoration: none;
}

.sidebar-btn img {
    width: 24px;
    margin-right: 10px;
}

.sidebar-footer {
    color: #DC3545;
}

.logo {
    margin-top: 0px;
    margin-bottom: 70px;
}

.logo-img {
    width: 90%;
}
</style>