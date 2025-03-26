<template>
  <div class="stock-alerts">
    <h2 class="history-heading">Stock Alerts</h2>
    <div class="table-container">
      <table>
        <thead>
          <tr>
            <th>Request Date</th>
            <th>Product</th>
            <th>Requested Quantity</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="alert in latestAlerts" :key="alert.request_date">
            <td>{{ formatDate(alert.request_date) }}</td>
            <td>{{ alert.product }}</td>
            <td>{{ alert.requested_quantity }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      stockAlerts: [],
    };
  },
  computed: {
    latestAlerts() {
      return this.stockAlerts.slice(0, 4); 
    }
  },
  created() {
    axios.get('http://127.0.0.1:8000/api/stock-alerts/')
      .then(response => {
        this.stockAlerts = response.data.reverse();
      })
      .catch(error => console.error(error));
  },
  methods: {
    formatDate(dateString) {
      if (!dateString) return ''; 
      return dateString.split('T')[0]; 
    }
  }
};
</script>
