import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

//import Vue from "vue";

//import Chartkick from "vue-chartkick";
//import Chart from "chart.js";

//Vue.use(Chartkick.use(Chart));

createApp(App)
  //.use(router, Chartkick.use(Chart))
  .use(router)
  .mount("#app");
