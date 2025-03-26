<template>
    <div class="main-container">
      <div id="dashboard" class="d-flex vh-100">
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

    <section class="main-content flex-grow-1 p-4 bg-light">
      <div class="heading">

  <h4 class="logo">Stockify</h4>

  <div class="header-icons">

    <div class="search-field">
      <img src="../assets/images/search.png" alt="Search" class="search-icon"> 
      <input type="text" placeholder="Search for anything here" />
    </div>

    <img src="../assets/images/notification.png" alt="Profile" class="app-main-icons">
    <img src="../assets/images/settings.png" alt="Profile" class="app-main-icons">
    
    <i class="fas fa-bell notification-icon"></i>
    <i class="fas fa-cog settings-icon"></i>
    <img src="" alt="" class="profile-pic">
  </div>
</div>

      
      <div class="row d-flex justify-content-between" style="margin-right: 50px;">
      <div class="col-md-4 top-banner">
        <div class="banner banner-sales d-flex align-items-start">
          <div class="content">
            <h4>Sales Overview</h4>
            <div class="details">
              <section class="full-labels-section">
                <div class="full-label">
                  <div class="icon-box">
                    <img src="../assets/images/dollar.png" alt="Sales Icon" class="icon" />
                  </div>
                  <div class="text-box">
                    <div class="label">Today Sales</div>
                    <div class="number">3,200</div>
                  </div>
                </div>

                <div class="full-label ms-3">
                  <div class="icon-box">
                    <img src="../assets/images/graph.png" alt="Sales Chart Icon" class="icon" />
                  </div>
                  <div class="text-box">
                    <div class="label">Total Sales</div>
                    <div class="number">26,600</div>
                  </div>
                </div>
              </section>
            </div>
          </div>
        </div>
      </div>

      <div class="col-md-4 top-banner">
        <div class="banner banner-sales d-flex align-items-start">
          <div class="content">
            <h4>Inventory Overview</h4>
            <div class="details">
              <section class="full-labels-section">
                <div class="full-label">
                  <div class="icon-box">
                    <img src="../assets/images/stock.png" alt="Stock Icon" class="icon" />
                  </div>
                  <div class="text-box">
                    <div class="label">Stock Available</div>
                    <div class="number">124</div>
                  </div>
                </div>

                <div class="full-label ms-3">
                  <div class="icon-box">
                    <img src="../assets/images/cart.png" alt="Sales Chart Icon" class="icon" />
                  </div>
                  <div class="text-box">
                    <div class="label">Sold Items</div>
                    <div class="number">1,264</div>
                  </div>
                </div>
              </section>
            </div>
          </div>
        </div>
      </div>

      <div class="col-md-4 top-banner " >
        <div class="banner banner-sales-dark d-flex align-items-start">
          <div class="content">
            <h4 style="color: white;">Inventory Insights</h4>
            <div class="details">
              <section class="full-labels-section" style="margin-right: 10px;">
                <div class="full-label">
                  <div class="icon-box">
                  </div>
                  <div class="text-box">
                    <div class="label" style="color: white;"> Total Expenses</div>
                    <div class="number" style="color: white;">11,200</div>
                  </div>
                </div>

                <div class="full-label ms-3">
                  <div class="icon-box">
                  </div>
                  <div class="text-box">
                    <div class="label" style="color: white;">Active Stock</div>
                    <div class="number" style="color: white;">26</div>
                  </div>
                </div>
              </section>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <div class="graphs-section-display">
    <div class="graph-display">
      <section >
      <SalesStockChart/>
    </section>
    </div>
    <div class="graph-display" style="width: -120px;">
      <section >
      <SalesDistributionPie/>
    </section>
    </div>
    </div>

    <div class="graphs-section-display">
      <div class="graph-display">
        <section >
          <StockHistory/>
      </section>
      </div>
      <div class="graph-display secon-dis">
        <section >
        <StockAlerts/>
      </section>
    </div>
  </div>

    </section>
    </div>
  </div>
      <router-view></router-view>
</template>

<script>

import SalesStockChart from "../components/SalesStockChart.vue";
import SalesDistributionPie from "../components/SalesDistributionPie.vue";
import StockHistory from '../pages/StockHistory.vue';
import StockAlerts from '../pages/StockAlerts.vue';

export default {
  name: "Dashboard",
  components: {
    SalesStockChart,
    SalesDistributionPie,
    StockHistory,
    StockAlerts,
  },
};
</script>
<style src="../assets/css/dashboard.css"></style>
