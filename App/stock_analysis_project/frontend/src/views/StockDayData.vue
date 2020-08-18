<template>
  <div class="container">
    <h1>StockDayData Component :</h1>

    <table id="firstTable">
      <thead>
        <tr>
          <th>Date</th>
          <th>company stock data</th>
          <th>Volume</th>
          <th>Close</th>
          <th>OBV</th>
          <th>Percent Change OBV</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in arr" :key="item.id">
          <td>{{ item.stock_date }}</td>
          <td>{{ item.ticker }}</td>
          <td>{{ item.volume }}</td>
          <td>{{ item.close }}</td>

          <td>{{ item.obv_change }}</td>
          <td>{{ item.percentage_change }}%</td>
        </tr>
      </tbody>
    </table>
    <h2>OBV percentage: {{ obv_perc_in }}</h2>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "StockDayData",
  props: {
    id: {
      required: true
    },
    obv_perc_in: {
      required: true
    }
  },
  computed: {
    // nicely look number of float for template
    get_obv_nice: function() {
      //return new Intl.NumberFormat().format(this.obv_percentege);
      return 10;
      //let nfObject = new Intl.NumberFormat("en-US");
      //return nfObject.format(givenNumber);
    }
  },

  data() {
    return {
      stockdaydata_list: {},
      before_item_vol: 0,
      obv_percentege: 1,

      arr: {}
    };
  },
  methods: {
    get_stockdaydata_list() {
      axios
        //.get(`/api/Company/StockDays/${this.id}`)
        .get(`/api/Company/StockDays/${this.id}/`)
        //.get("blah/blah")
        //.then(response => (this.stockdaydata_list = response.data.results));

        .then(
          response =>
            (this.arr = response.data.results.map(item => {
              const container = {};

              container["stock_date"] = item.stock_date;
              container["id"] = item.id;
              container["close"] = item.close;
              container["ticker"] = item.company_stock_data.ticker;
              container["volume"] = item.volume;

              // calculate percent change , and obv diffrence from day x to day x-1

              if (this.before_item_vol == 0 || item.volume == 0) {
                container["obv_change"] = item.volume + this.before_item_vol;
                // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat
                container["percentage_change"] = new Intl.NumberFormat().format(
                  0
                );
                this.before_item_vol = item.volume;
                return container;
              }

              let sum = this.before_item_vol;

              if (item.volume >= this.before_item_vol) {
                sum += item.volume;
                this.obv_percentege += item.volume / this.before_item_vol;
                container["percentage_change"] = new Intl.NumberFormat().format(
                  ((item.volume - this.before_item_vol) /
                    this.before_item_vol) *
                    100
                );
              } else {
                sum -= item.volume;
                this.obv_percentege -= this.before_item_vol / item.volume;
                container["percentage_change"] = new Intl.NumberFormat().format(
                  ((this.before_item_vol - item.volume) /
                    this.before_item_vol) *
                    -100
                );
              }
              this.before_item_vol = item.volume;
              //return sum;

              container["obv_change"] = sum;

              return container;
            }))
        );

      // trim numbers after dot

      //console.log("arr " + this.arr);
    }
  },

  created() {
    this.get_stockdaydata_list();
    //alert(" aa " + this.stockdaydata_list);
    //console.log(" -- " + this.stockdaydata_list);
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
table {
  font-family: "Open Sans", sans-serif;
  width: 70%;
  border-collapse: collapse;
  border: 3px solid #44475c;
  margin: 10px 10px 0 10px;
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
