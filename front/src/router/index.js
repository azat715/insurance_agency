import { createRouter, createWebHistory } from 'vue-router';
import Products from '../views/Products.vue';

const routes = [
  {
    path: '/',
    name: 'Products',
    component: Products,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
