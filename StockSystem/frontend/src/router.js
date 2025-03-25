import { createRouter, createWebHistory } from 'vue-router'
import Home from './pages/Home.vue';
import Login from './pages/Login.vue';
import StockAlerts from './pages/StockAlerts.vue';
import SalesEntries from './pages/SalesEntries.vue';
import StockHistory from './pages/StockHistory.vue';
import Inventory from './pages/Inventory.vue';
import Register from './pages/Register.vue';
import Dashboard from './pages/Dashboard.vue';
import SalesStockChart from './components/SalesStockChart.vue';
import SalesDistributionPie from './components/SalesDistributionPie.vue';
import BaseLayout from './components/BaseLayout.vue';


const routes = [
  {path: '/',name: 'home',component: Home,},
  {path: '/login',name: 'login',component: Login,},
  {path: '/register',name: 'register',component: Register,},
  { path: '/', redirect: '/inventory' },
  { path: '/stock-alerts', component: StockAlerts },
  { path: '/sales-entries', component: SalesEntries },
  { path: '/stock-history', component: StockHistory },
  { path: '/inventory', component: Inventory },
  { path: '/dashboard', component: Dashboard },
  { path: '/SalesStockChart', component: SalesStockChart },
  { path: '/SalesDistributionPie', component: SalesDistributionPie },
  { path: '/BaseLayout', component: BaseLayout },]
  
const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router