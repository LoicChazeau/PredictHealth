<template>
    <aside class="sidebar">
        <div class="logo">
            <img src="../assets/logo.svg" alt="PredictHealth" class="logo-img">
        </div>
        <div class="sidebar-container">
            <div class="sidebar-content">
                <router-link to="/" class="sidebar-btn" active-class="active">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"
                        xmlns="http://www.w3.org/2000/svg">
                        <path
                            d="M19 5V7H15V5H19ZM9 5V11H5V5H9ZM19 13V19H15V13H19ZM9 17V19H5V17H9ZM21 3H13V9H21V3ZM11 3H3V13H11V3ZM21 11H13V21H21V11ZM11 15H3V21H11V15Z" />
                    </svg>
                    <span>Accueil</span>
                    <div class="active-indicator"></div>
                </router-link>
                <router-link to="/admissions" class="sidebar-btn" active-class="active">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"
                        xmlns="http://www.w3.org/2000/svg">
                        <path
                            d="M20 4V16H8V4H20ZM20 2H8C6.9 2 6 2.9 6 4V16C6 17.1 6.9 18 8 18H20C21.1 18 22 17.1 22 16V4C22 2.9 21.1 2 20 2ZM11.5 11.67L13.19 13.93L15.67 10.83L19 15H9L11.5 11.67ZM2 6V20C2 21.1 2.9 22 4 22H18V20H4V6H2Z" />
                    </svg>
                    <span>Admissions</span>
                    <div class="active-indicator"></div>
                </router-link>
                <router-link to="/previsions" class="sidebar-btn" active-class="active">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"
                        xmlns="http://www.w3.org/2000/svg">
                        <path
                            d="M19 3H18V1H16V3H8V1H6V3H5C3.89 3 3.01 3.9 3.01 5L3 19C3 20.1 3.89 21 5 21H19C20.1 21 21 20.1 21 19V5C21 3.9 20.1 3 19 3ZM19 19H5V9H19V19ZM19 7H5V5H19V7ZM17 12H12V17H17V12Z" />
                    </svg>
                    <span>Prévisions</span>
                    <div class="active-indicator"></div>
                </router-link>
                <router-link to="/recommandations" class="sidebar-btn" active-class="active">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"
                        xmlns="http://www.w3.org/2000/svg">
                        <path
                            d="M9 24.75H18C18.83 24.75 19.54 24.1875 19.84 23.3775L22.86 15.4462C22.95 15.1875 23 14.9175 23 14.625V12.375C23 11.1375 22.1 10.125 21 10.125H14.69L15.64 4.98375L15.67 4.62375C15.67 4.1625 15.5 3.735 15.23 3.43125L14.17 2.25L7.58 9.66375C7.22 10.0688 7 10.6313 7 11.25V22.5C7 23.7375 7.9 24.75 9 24.75ZM9 11.25L13.34 6.3675L12 12.375H21V14.625L18 22.5H9V11.25ZM1 11.25H5V24.75H1V11.25Z" />
                    </svg>
                    <span>Recommandations</span>
                    <div class="active-indicator"></div>
                </router-link>
                <router-link to="/parametres" class="sidebar-btn" active-class="active">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"
                        xmlns="http://www.w3.org/2000/svg">
                        <path
                            d="M19.43 12.98C19.47 12.66 19.5 12.34 19.5 12C19.5 11.66 19.47 11.34 19.43 11.02L21.54 9.37C21.73 9.22 21.78 8.95 21.66 8.73L19.66 5.27C19.57 5.11 19.4 5.02 19.22 5.02C19.16 5.02 19.1 5.03 19.05 5.05L16.56 6.05C16.04 5.65 15.48 5.32 14.87 5.07L14.49 2.42C14.46 2.18 14.25 2 14 2H10C9.75002 2 9.54002 2.18 9.51002 2.42L9.13002 5.07C8.52002 5.32 7.96002 5.66 7.44002 6.05L4.95002 5.05C4.89002 5.03 4.83002 5.02 4.77002 5.02C4.60002 5.02 4.43002 5.11 4.34002 5.27L2.34002 8.73C2.21002 8.95 2.27002 9.22 2.46002 9.37L4.57002 11.02C4.53002 11.34 4.50002 11.67 4.50002 12C4.50002 12.33 4.53002 12.66 4.57002 12.98L2.46002 14.63C2.27002 14.78 2.22002 15.05 2.34002 15.27L4.34002 18.73C4.43002 18.89 4.60002 18.98 4.78002 18.98C4.84002 18.98 4.90002 18.97 4.95002 18.95L7.44002 17.95C7.96002 18.35 8.52002 18.68 9.13002 18.93L9.51002 21.58C9.54002 21.82 9.75002 22 10 22H14C14.25 22 14.46 21.82 14.49 21.58L14.87 18.93C15.48 18.68 16.04 18.34 16.56 17.95L19.05 18.95C19.11 18.97 19.17 18.98 19.23 18.98C19.4 18.98 19.57 18.89 19.66 18.73L21.66 15.27C21.78 15.05 21.73 14.78 21.54 14.63L19.43 12.98ZM17.45 11.27C17.49 11.58 17.5 11.79 17.5 12C17.5 12.21 17.48 12.43 17.45 12.73L17.31 13.86L18.2 14.56L19.28 15.4L18.58 16.61L17.31 16.1L16.27 15.68L15.37 16.36C14.94 16.68 14.53 16.92 14.12 17.09L13.06 17.52L12.9 18.65L12.7 20H11.3L11.11 18.65L10.95 17.52L9.89002 17.09C9.46002 16.91 9.06002 16.68 8.66002 16.38L7.75002 15.68L6.69002 16.11L5.42002 16.62L4.72002 15.41L5.80002 14.57L6.69002 13.87L6.55002 12.74C6.52002 12.43 6.50002 12.2 6.50002 12C6.50002 11.8 6.52002 11.57 6.55002 11.27L6.69002 10.14L5.80002 9.44L4.72002 8.6L5.42002 7.39L6.69002 7.9L7.73002 8.32L8.63002 7.64C9.06002 7.32 9.47002 7.08 9.88002 6.91L10.94 6.48L11.1 5.35L11.3 4H12.69L12.88 5.35L13.04 6.48L14.1 6.91C14.53 7.09 14.93 7.32 15.33 7.62L16.24 8.32L17.3 7.89L18.57 7.38L19.27 8.59L18.2 9.44L17.31 10.14L17.45 11.27ZM12 8C9.79002 8 8.00002 9.79 8.00002 12C8.00002 14.21 9.79002 16 12 16C14.21 16 16 14.21 16 12C16 9.79 14.21 8 12 8ZM12 14C10.9 14 10 13.1 10 12C10 10.9 10.9 10 12 10C13.1 10 14 10.9 14 12C14 13.1 13.1 14 12 14Z" />
                    </svg>
                    <span>Paramètres</span>
                    <div class="active-indicator"></div>
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
    width: 250px;
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
    color: #8489A5;
    text-decoration: none;
    position: relative;
    border-radius: 8px;
    transition: all 0.3s ease-in-out;
}

.sidebar-btn svg {
    width: 24px;
    margin-right: 10px;
    color: #8489A5;
    transition: all 0.3s ease-in-out;
}

.sidebar-btn.active {
    color: #333B6A;
}

.sidebar-btn.active svg {
    color: #333B6A;
}

.sidebar-btn.active .active-indicator {
    position: absolute;
    right: -20px;
    top: 50%;
    transform: translateY(-50%);
    width: 8px;
    height: 24px;
    background: #333B6A;
    border-radius: 12px 0 0 12px;
}

.sidebar-footer {
    color: #DC3545;
}

.logo {
    margin-top: 0px;
    margin-bottom: 70px;
}

.logo-img {
    width: 95%;
}
</style>