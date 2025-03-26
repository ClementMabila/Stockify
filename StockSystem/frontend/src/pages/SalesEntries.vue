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
          <button class="entry-icon-button-black" @click="showModal = true">
            <img src="../assets/images/plus.png" alt="Add" class="entry-icons">
            <span> Add Entry</span>
          </button>

          <div v-if="showModal" class="modal-overlay">
            <div class="modal-content">
              <label>Product ID:</label>
              <input type="number" v-model="newSale.product" required>

              <label>Customer ID:</label>
              <input type="number" v-model="newSale.customer" required>

              <label>SKU:</label>
              <input type="text" v-model="newSale.sku" required>

              <label>Quantity Sold:</label>
              <input type="number" v-model="newSale.quantity_sold" required>

              <label>Sale Price:</label>
              <input type="number" step="0.01" v-model="newSale.sale_price" required>

              <label>Status:</label>
              <select v-model="newSale.status">
                <option value="Completed">Completed</option>
                <option value="Pending">Pending</option>
                <option value="Cancelled">Cancelled</option>
              </select>

              <div class="modal-actions">
                <button class="modal-buttons" @click="submitSale">Submit</button>
                <button class="modal-buttons" @click="showModal = false">Cancel</button>
              </div>
            </div>
          </div>

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
            <td class="status-td">
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
      showModal: false,
      newSale: {
        product: '',
        customer: '',
        sku: '',
        quantity_sold: '',
        sale_price: '',
        status: 'Completed'
      }
    };
  },
  created() {
    this.fetchSalesEntries();
  },
  methods: {
    async fetchSalesEntries() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/sales-entries/');
        this.salesEntries = response.data;
      } catch (error) {
        console.error("Error fetching sales entries:", error);
      }
    },
    getStatusClass(status) {
      return {
        'status-completed': status === 'Completed',
        'status-pending': status === 'Pending',
        'status-cancelled': status === 'Cancelled'
      };
    },
    async submitSale() {
   try {
     const response = await axios.post('http://127.0.0.1:8000/api/sales-entries/', {
       product: parseInt(this.newSale.product),
       customer: parseInt(this.newSale.customer),  // Make sure customer is included
       sku: this.newSale.sku,
       quantity_sold: parseInt(this.newSale.quantity_sold),
       sale_price: parseFloat(this.newSale.sale_price),
       status: this.newSale.status
     });

     console.log('Sale Added:', response.data);
     alert('Sale entry added successfully!');

     this.fetchSalesEntries();

     this.showModal = false;
     this.newSale = {  // Reset form after submission
       product: '',
       customer: '',
       sku: '',
       quantity_sold: '',
       sale_price: '',
       status: 'Completed'
     };
   } catch (error) {
     console.error('Error:', error.response?.data || error);
     alert('Failed to add sale entry.');
   }
}
  }
};
</script>
