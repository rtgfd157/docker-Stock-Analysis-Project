import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";

import OBVindex from "../views/OBVindex.vue";
import StockDayData from "../views/StockDayData.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/stockdaydata/:id/:obv_perc_in",
    name: "StockdayData",
    component: StockDayData,
    props: true
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue")
  },
  {
    path: "/OBVindex",
    name: "OBVindex",
    component: OBVindex
  }
];

/*
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});
*/

const router = createRouter({
  history: createWebHistory(),
  routes
});
export default router;
