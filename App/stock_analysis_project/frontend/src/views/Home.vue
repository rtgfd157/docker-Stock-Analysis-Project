<template>
  <div class="home">
    <h2>Home Component:</h2>
    <h2>Number of Stockdata : {{ counter_list.stockdata_count }}</h2>

    <h2>Number of Companies : {{ counter_list.company_count }}</h2>

    <button class="btn btn-secondary" v-on:click="delete_db">
      Delete All DB
    </button>
    <button class="btn btn-secondary" v-on:click="load_db">
      Load DB
    </button>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from "axios";
import { apiService } from "../common/api.service";

export default {
  name: "Home",

  data() {
    return {
      counter_list: {}
    };
  },
  methods: {
    get_company_stockdata_count() {
      //let var1;
      axios
        .get(`/api/Company/StockDay/counter/`)
        .then(response => (this.counter_list = response.data));

      //console.log("  -- " + this.counter_list);
      // alert("1  " + var1);
    },
    async delete_db() {
      //axios.get("/delete_all_db/");
      let endpoint = "delete_all_db/";
      await apiService(endpoint);

      alert("delete db");
      this.get_company_stockdata_count(); // update count
    },
    async load_db() {
      let endpoint = "load_db/";
      await apiService(endpoint);

      alert("load db");
      this.get_company_stockdata_count(); // update count
    }
  },
  created() {
    this.get_company_stockdata_count();
    //alert(" aa " + this.stockdaydata_list);
    //console.log(" -- " + this.stockdaydata_list);
  }
};
</script>
