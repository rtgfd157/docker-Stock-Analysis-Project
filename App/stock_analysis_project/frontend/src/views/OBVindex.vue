<template>
  <div class="example">
    <h2>OBV index</h2>

    <div>
      <button class="btn btn-secondary" v-on:click="update_list">
        Update List
      </button>
      <button class="btn btn-link" @click="printData()">
        Print Data
      </button>
      <div class="row">
        <table id="firstTable">
          <thead>
            <tr>
              <th>company stock data</th>
              <th>obv rate</th>
              <th>percentage change</th>
              <th>Link Yahoo Finance</th>
              <th>Stock Day Data</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="obv in obv_index_list" :key="obv.pk">
              <td>
                {{ obv.company_stock_data.ticker }} -
                {{ obv.company_stock_data.company_name }}
              </td>
              <td>{{ obv.obv }}</td>
              <td>{{ obv.percentage_change }}</td>
              <td>
                <button
                  class="btn btn-link"
                  @click="myFunction(obv.company_stock_data)"
                >
                  yahoo@{{ obv.company_stock_data.ticker }}
                </button>
              </td>
              <td>
                <router-link
                  :to="{
                    name: 'StockdayData',
                    params: {
                      id: obv.company_stock_data.id,
                      obv_perc_in: obv.percentage_change
                    }
                  }"
                >
                  Stock Day Data
                </router-link>
              </td>
            </tr>
          </tbody>
        </table>
        <container>
          <p>Percentage of change</p>
          <BarChart
            class="chart"
            v-bind:data-set="data_percentage_change"
            :margin-left="40"
            :margin-top="40"
            :tick-count="5"
            :bar-padding="0.5"
          />

          <p>Volume of exchange</p>
          <BarChart
            class="chart"
            v-bind:data-set="data_volume_change"
            :margin-left="40"
            :margin-top="40"
            :tick-count="5"
            :bar-padding="0.5"
          />
        </container>
      </div>
      <br />
    </div>
  </div>
</template>

<script>
import { apiService } from "../common/api.service";
import BarChart from "@/components/BarChart.vue";

export default {
  name: "OBVindex",
  components: {
    BarChart
  },

  created() {
    this.getOBVindex();
  },

  data() {
    return {
      // Array will be automatically processed with visualization.arrayToDataTable function
      data_percentage_change: [],

      data_volume_change: [],
      // list that will be in thae table of 10 best OBV stocks by percentage change
      obv_index_list: []
    };
  },

  methods: {
    printData() {
      //alert("11 " + this.obv_index_list);

      this.data_percentage_change = this.obv_index_list.map(item => {
        const container = {};

        //alert(" -- " + item);
        container[0] = item.company_stock_data.ticker;
        container[1] = item.percentage_change;

        return container;
      });
      //alert(this.data);

      //alert(this.obv_index_list);
    },
    myFunction(a) {
      // open link in yahoo finance
      window.open(`https://finance.yahoo.com/quote/${a.ticker}`, "_blank");
    },
    getOBVindex() {
      // get OBV index list from server
      let endpoint = "api/OBVindex/";
      apiService(endpoint).then(data => {
        this.obv_index_list.push(...data.results);
        //this.data = this.obv_index_list;

        // data of percentage change
        this.data_percentage_change = data.results.map(item => {
          const container = {};

          container[0] = item.company_stock_data.ticker;
          container[1] = item.percentage_change;
          return container;
        });

        //  date of volume
        this.data_volume_change = data.results.map(item => {
          const container = {};

          container[0] = item.company_stock_data.ticker;
          container[1] = item.obv;
          return container;
        });
      });
    },
    async update_list() {
      // update 10 best OBV stock on db using backend  evalution script
      let endpoint = "obv_index_maker_view/";
      apiService(endpoint);
      alert("Updating obv index " + this.name + "!");
    }
  }
};
</script>

<style scoped>
.row {
  margin: 5px 5px 0 5px;
}
table {
  font-family: "Open Sans", sans-serif;
  width: 60%;
  border-collapse: collapse;
  border: 3px solid #44475c;
  margin: 20px 10px 0 10px;
}

table th {
  text-transform: uppercase;
  text-align: left;
  background: #44475c;
  color: #fff;
  padding: 8px;
  min-width: 30px;
}

table td {
  text-align: left;
  padding: 8px;
  border-right: 2px solid #7d82a8;
}
table td:last-child {
  border-right: none;
}
table tbody tr:nth-child(2n) td {
  background: #d4d8f9;
}
</style>
