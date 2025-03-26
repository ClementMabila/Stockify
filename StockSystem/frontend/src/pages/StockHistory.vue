<template>
  <div class="stock-history-container">
    <h4 class="history-heading">Recent Purchases</h4>
    <div class="table-container">
      <table>
        <thead>
          <tr>
            <th>Transaction Date</th>
            <th>Category</th>
            <th>Product</th>
            <th>Uruantial Revenue</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="history in latestStockHistory" :key="history.id">
            <td>{{ formatDate(history.transaction_date) }}</td>
            <td>{{ history.transaction_type }}</td>
            <td>{{ history.product }}</td>
            <td>${{ parseFloat(history.total_revenue).toFixed(2) }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      stockHistory: [],
    };
  },
  created() {
    axios
      .get("http://127.0.0.1:8000/api/stock-history/")
      .then((response) => {
        this.stockHistory = response.data;
      })
      .catch((error) => console.error(error));
  },
  computed: {
    latestStockHistory() {
      return this.stockHistory.slice(0, 3);
    },
  },
  methods: {
    formatDate(date) {
      return new Date(date).toLocaleString();
    },
  },
};
</script>

<style src="../assets/css/dashboard.css"></style>
