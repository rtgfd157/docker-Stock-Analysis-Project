<template>
  <div id="app">
    <div class="container">
      <router-link to="/OBVindex"> OBV index</router-link>
      <router-link to="/about"> about</router-link>
      <router-link to="/"> Home</router-link>
    </div>
    <button class="btn btn-primary" v-on:click="update_stockdays_data">
      Update Daily Stock Data
    </button>

    <!-- router view will show content of router link -->
    <router-view />
  </div>
</template>

<script>
import { apiService } from "./common/api.service";
import axios from "axios";

export default {
  name: "App",

  data() {
    return {
      //counter_list: {}
    };
  },

  methods: {
    update_stockdays_data() {
      // update all stocks daily  close , volume  - to 5 day long
      //let companies = -1;
      axios
        .get(`/api/Company/StockDay/counter/`)
        .then(response =>
          this.update_stock_day_data(response.data.company_count)
        );

      // refresh page after change
      // https://stackoverflow.com/questions/48503760/vue-js-router-link-with-a-function-inside
      // https://router.vuejs.org/guide/essentials/navigation.html
      this.$router.push("/");
    },

    update_stock_day_data(val) {
      if (val > 0) {
        let endpoint = "celerytask/";
        apiService(endpoint);
        alert("Updating Stock Day Data " + val);
      } else {
        alert("We have 0 companies so we cant update empty value " + val);
      }
    }
  },
  created() {
    //this.get_company_stockdata_count();
    //alert(" aa " + this.stockdaydata_list);
    //console.log(" -- " + this.stockdaydata_list);
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
