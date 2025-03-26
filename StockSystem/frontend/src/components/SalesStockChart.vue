<template>
  <div class="p-4 bg-white rounded-lg shadow-md" style="margin-top: 20px;">
    <!-- Header & Year Selection -->
    <div class="flex justify-between items-center mb-4">
      <h2 class="text-lg bar-title font-semibold" style="font-weight: bold;">Sales & Stock Comparison</h2>
      <select v-model="selectedYear" class="border p-2 rounded">
        <option v-for="year in availableYears" :key="year" :value="year">{{ year }}</option>
      </select>
    </div>

    <!-- Legend -->
    <div class="flex gap-4 mb-2">
      <div class="flex items-center">
        <div class="w-4 h-4 bg-black rounded-sm mr-2"></div>
        <span class="text-sm">Sales</span>
      </div>
      <div class="flex items-center">
        <div class="w-4 h-4 bg-gray-500 rounded-sm mr-2"></div>
        <span class="text-sm">Stock</span>
      </div>
    </div>

    <!-- Chart -->
    <div class="chart-container">
      <canvas id="myChart"></canvas>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref, computed, onMounted } from "vue";
import { Chart, BarController, BarElement, CategoryScale, LinearScale, Tooltip, Legend } from "chart.js";

// Register the required controllers and elements
Chart.register(BarController, BarElement, CategoryScale, LinearScale, Tooltip, Legend);

export default defineComponent({
  setup() {
    const selectedYear = ref("2024");

    const salesData = {
      2022: [
        { month: "Jan", Sales: 1200, Stock: 2000 },
        { month: "Feb", Sales: 2500, Stock: 3800 },
        { month: "Mar", Sales: 1700, Stock: 1600 },
        { month: "Apr", Sales: 3200, Stock: 1400 },
        { month: "May", Sales: 3600, Stock: 1200 },
        { month: "Jun", Sales: 2900, Stock: 1000 },
      ],
      2023: [
        { month: "Jan", Sales: 2100, Stock: 1000 },
        { month: "Feb", Sales: 3100, Stock: 4100 },
        { month: "Mar", Sales: 1700, Stock: 1200 },
        { month: "Apr", Sales: 3300, Stock: 1500 },
        { month: "May", Sales: 1600, Stock: 1200 },
        { month: "Jun", Sales: 1900, Stock: 1000 },
      ],
      2024: [
        { month: "Jan", Sales: 3200, Stock: 5000 },
        { month: "Feb", Sales: 4500, Stock: 4800 },
        { month: "Mar", Sales: 3700, Stock: 4600 },
        { month: "Apr", Sales: 4200, Stock: 4400 },
        { month: "May", Sales: 4600, Stock: 4200 },
        { month: "Jun", Sales: 4900, Stock: 4000 },
      ],
    };

    const chartData = computed(() => {
      const filteredData = salesData[selectedYear.value] || [];
      return {
        labels: filteredData.map((d) => d.month),
        datasets: [
          {
            label: "Sales",
            data: filteredData.map((d) => d.Sales),
            backgroundColor: "black",
            barThickness: 20, 
            maxBarThickness: 20, 
            borderRadius: 2, 
          },
          {
            label: "Stock",
            data: filteredData.map((d) => d.Stock),
            backgroundColor: "gray",
            barThickness: 20,
            maxBarThickness: 20,
            borderRadius: 2,
          },
        ],
      };
    });

    const chartOptions = {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          display: false, // Disable the legend
        },
      },
      scales: {
        x: {
          grid: {
            display: false,
          },
          categoryPercentage: 0.8,
          barPercentage: 5, 
        },
        y: {
          beginAtZero: true,
          grid: {
            color: "#e0e0e0", 
          },
        },
      },
    };

    onMounted(() => {
      const ctx = document.getElementById("myChart").getContext("2d");
      new Chart(ctx, {
        type: "bar",
        data: chartData.value,
        options: chartOptions,
      });
    });

    return { selectedYear, chartData, chartOptions, availableYears: Object.keys(salesData) };
  },
});
</script>

<style scoped>
.chart-container {
  height: 170px;
  width: 100%;
}
</style>
<style src="../assets/css/dashboard.css"></style>