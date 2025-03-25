<template>
  <BaseLayout>
    <div class="sales-entrie-container">
      <h2 class="entry-header">Sales Entry</h2>
      <div class="sales-actions">
        <div class="search-field">
          <img src="../assets/images/search.png" alt="Search" class="search-icon">
          <input type="text" placeholder="Search Entry..." />
        </div>
        <div class="header-entry-icons">
          <button class="entry-icon-button" @click="toggleFilter">
            <img src="../assets/images/filter.png" alt="Search" class="entry-icons">
            <span> Filter</span>
          </button>
          <button class="entry-icon-button-black" @click="addNewEntry">
            <img src="../assets/images/plus.png" alt="Search" class="entry-icons">
            <span> Add Entry</span>
          </button>
        </div>
      </div>
      <table>
        <thead>
          <tr>
            <th class="sales-entry-th">Date</th>
            <th class="sales-entry-th">Product</th>
            <th class="sales-entry-th">SKU</th>
            <th class="sales-entry-th">Quantity</th>
            <th class="sales-entry-th">Unit Price</th>
            <th class="sales-entry-th">Status</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="sale in salesEntries" :key="sale.id" class="sales-entry-tr">
            <td>{{ new Date(sale.sale_date).toLocaleDateString() }}</td>
            <td>{{ sale.product }}</td>
            <td>{{ sale.sku }}</td>
            <td>{{ sale.quantity_sold }}</td>
            <td>${{ sale.sale_price }}</td>
            <td>
  <span 
    class="status-box" 
    :class="getStatusClass(sale.status)"
  ></span>
  <span 
    class="status-text"
    :class="getStatusClass(sale.status)"
  >
    {{ sale.status }}
  </span>
</td>


          </tr>
        </tbody>
      </table>
    </div>
  </BaseLayout>
</template>

<script>
import axios from 'axios';
import BaseLayout from "../components/BaseLayout.vue";

export default {
  name: "SalesEntriesPage",
  components: {
    BaseLayout,
  },
  data() {
    return {
      salesEntries: [],
    };
  },
  created() {
    axios.get('http://127.0.0.1:8000/api/sales-entries/')
      .then(response => {
        this.salesEntries = response.data;
      })
      .catch(error => console.error(error));
  },
  methods: {
    getStatusClass(status) {
      return {
        'status-completed': status === 'Completed',
        'status-pending': status === 'Pending',
        'status-cancelled': status === 'Cancelled'
      };
    }
  }
};
</script>
