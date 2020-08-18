from Main_app.models import ComapnyStockData, StockDayData
from .models import OBVindex
import time

class ObvIndexMakerClass:
    """
    class that make OBV  index of 10 most high obv percentages changes over last 5 days.
    """

    def __init__(self):
        """
        init making run
        """
        self.all_stockday_data = StockDayData.objects.prefetch_related(
            'company_stock_data').all()
        self.OBV_index_l = []  # empty list that will hold the index

        self.bol_exceed_10 = False  # for speed testing purpose

        
    def make(self):
        """
        main function of ObvIndexMaker, that will run class functionality ...
        make and insert OBV values
        """
        self.companies_stock_data = self.all_stockday_data.distinct().values_list(
            'company_stock_data', flat=True)  # var of distinct companies
        start_time = time.time()
        print("_____________")

        print("_____________")

        counter = 0
        for company in self.companies_stock_data:
            counter += 1
            obv_percentege = 1  # percent change of obv index over  a week
            obv = 0  # obv index value ,  start from 0
            stockdays_data_for_company = self.all_stockday_data.filter(
                company_stock_data__id=company).order_by('stock_date').values_list('volume', flat=True)
            # the oldest  stock data date -  we will get list of volumes 

            #before_vol = stockdays_data_for_company[0]  # first value in a list
            before_vol = 0
            # loop days with stock data for comapny -- set obv , volume rate
            for stockday_data_for_company in stockdays_data_for_company.iterator():
                obv, obv_percentege, before_vol = self.obv_obv_percentege_calc(
                    obv, stockday_data_for_company, before_vol, obv_percentege)

            # if company  good enough for index  -- check if company rates good for OBV_index_l
            self.obv_percentege_good_for_index_check(
                obv_percentege, obv, company)

        print(self.OBV_index_l)
        print("--- {}  TIME  (end) --- {}".format(time.time() - start_time, counter))

    def obv_percentege_good_for_index_check(self, obv_percentege, obv, company_id):
        """
        check if obv percentage is good enough for index
        if good enough will be inserted to OBV_index_l - list for being inserted in the end of all  companies looping
        """

        if not self.bol_exceed_10 and len(self.OBV_index_l) < 10:
            co = ComapnyStockData.objects.get(id=company_id)
            obv_val = OBVindex(company_stock_data=co,
                               percentage_change=obv_percentege, obv=obv)
            self.OBV_index_l.append(obv_val)
            # print(self.OBV_index_l)

            # for i in range(len(self.OBV_index_l)):
            #     print("{}) * COMPANY:{}  percent change:{}  obv: {} ".format(i,self.OBV_index_l[i].company_stock_data,  self.OBV_index_l[i].percentage_change, self.OBV_index_l[i].obv))
            # print("__________________2-")
            self.OBV_index_l = sorted(
                self.OBV_index_l, reverse=True, key=lambda x: x.percentage_change)

        else:
            weakest_com_in = self.OBV_index_l[len(self.OBV_index_l)-1]
            if weakest_com_in.percentage_change < obv_percentege:
                co = ComapnyStockData.objects.get(id=company_id)
                obv_val = OBVindex(company_stock_data=co,
                                   percentage_change=obv_percentege, obv=obv)

                self.OBV_index_l.pop()
                self.OBV_index_l.append(obv_val)
                # for i in range(len(self.OBV_index_l)):
                #     print("{}) * COMPANY:{}  percent change:{}  obv: {} ".format(i,self.OBV_index_l[i].company_stock_data,  self.OBV_index_l[i].percentage_change, self.OBV_index_l[i].obv))
                # print("__________________1-")
                self.OBV_index_l = sorted(
                    self.OBV_index_l, reverse=True, key=lambda x: x.percentage_change)

    def obv_obv_percentege_calc(self, obv, volume, before_vol, obv_percentege):
        """
        calc obv , obv_percentage
        """
        #obv += volume

        if before_vol == 0 or volume == 0:
            return obv+volume, obv_percentege, volume

        #return (obv+volume), (obv_percentege + (volume / before_vol)) if volume >= before_vol else (obv_percentege + (before_vol / volume)), volume
        sum_obv = before_vol # will be new obv volume
        if volume >= before_vol:

            obv_percentege += volume / before_vol
            sum_obv += volume
        else:
            obv_percentege -= before_vol / volume
            sum_obv -= volume
        before_vol = volume

        return sum_obv, obv_percentege, before_vol
