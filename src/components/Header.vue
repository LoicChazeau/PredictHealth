<template>
    <header class="header">
        <div class="notification">
            <img src="../assets/notification.svg" alt="Notification" class="notification-img" />
        </div>
        <div class="avatar">
            <img src="../assets/avatar.png" alt="Avatar" class="avatar-img" />
        </div>
    </header>
</template>

<script setup>
</script>

<style scoped>
.header {
    display: flex;
    justify-content: end;
    align-items: center;
    background: #e2e1e9;
    height: 80px;
    padding-right: 40px;
}

.notification {
    display: flex;
    align-items: center;
    margin-right: 20px;
}

.notification-img {
    width: 24px;
    height: 24px;
}

.avatar {
    display: flex;
    align-items: center;
}

.avatar-img {
    width: 35px;
    height: 35px;
    border-radius: 50%;
}
</style>