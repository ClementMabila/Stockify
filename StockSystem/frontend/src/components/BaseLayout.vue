<template>
    <div class="main-container">
      <div id="dashboard" class="d-flex vh-100">
        <!-- Sidebar -->
        <div class="sidebar">
          <ul class="nav flex-column">
            <li class="nav-item">
              <router-link to="/dashboard" class="nav-link">Dashboard</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/sales-entries" class="nav-link">Sales Entry</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/stock-history" class="nav-link-free">Stock History</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/inventory" class="nav-link-free">Inventory</router-link>
            </li>
          </ul>
        </div>
  
        <!-- Main Content -->
        <section class="main-content flex-grow-1 p-4 bg-light">
          <!-- Top Bar -->
          <div class="heading">
            <h4 class="logo">Stockify</h4>
            <div class="header-icons">
              <div class="search-field">
                <img src="../assets/images/search.png" alt="Search" class="search-icon"> 
                <input type="text" placeholder="Search for anything here" />
              </div>
              <img src="../assets/images/notification.png" alt="Notification" class="app-main-icons">
              <img src="../assets/images/settings.png" alt="Settings" class="app-main-icons">
              <i class="fas fa-bell notification-icon"></i>
              <i class="fas fa-cog settings-icon"></i>
              <img src="" alt="" class="profile-pic">
            </div>
          </div>
  
          <!-- Dynamic Content -->
          <slot></slot>
        </section>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "BaseLayout",
  };
  </script>
  
  <style src="../assets/css/dashboard.css"></style>
  