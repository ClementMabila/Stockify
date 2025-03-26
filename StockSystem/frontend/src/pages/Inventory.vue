<template>
    <div>
      <h2>Inventory</h2>
      <table>
        <thead>
          <tr>
            <th>Product</th>
            <th>Category</th>
            <th>SKU</th>
            <th>Available Size</th>
            <th>Unit Price</th>
            <th>Location</th>
            <th>Total Revenue</th>
            <th>Reorder Level</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="product in inventory" :key="product.sku">
            <td>{{ product.name }}</td>
            <td>{{ product.category }}</td>
            <td>{{ product.sku }}</td>
            <td>{{ product.available_size }}</td>
            <td>${{ product.unit_price }}</td>
            <td>{{ product.location }}</td>
            <td>${{ product.total_revenue }}</td>
            <td>{{ product.reorder_level }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        inventory: [],
      };
    },
    created() {
      axios.get('http://127.0.0.1:8000/api/inventory/')
        .then(response => {
          this.inventory = response.data;
        })
        .catch(error => console.error(error));
    }
  };
  </script>
  