from django.db import models
from Main_app.models import ComapnyStockData


class OBVindex(models.Model):
    """
        https://www.investopedia.com/terms/o/onbalancevolume.asp
        will hold best 10  obv = volume percentage best growth for the 10 days.

        1. If today's closing price is higher than yesterday's closing price, then: Current OBV = Previous OBV + today's volume.

        2. If today's closing price is lower than yesterday's closing price, then: Current OBV = Previous OBV - today's volume.

        3. If today's closing price equals yesterday's closing price, then: Current OBV = Previous OBV.

        should be 1 value per each comapny stock in 10 best OBV change in DB.
    """

    company_stock_data = models.ForeignKey(ComapnyStockData, on_delete=models.CASCADE)

    percentage_change = models.DecimalField(
        max_digits=13, decimal_places=2, verbose_name="Percentage Change")

    obv = models.DecimalField(
        max_digits=13, decimal_places=2, verbose_name="Volume Amount Change")

    def __str__(self):
        return  str(self.company_stock_data)+" " +str(self.percentage_change) + " " + str(self.obv)

    class Meta:
        verbose_name = 'OBV Stock'
        verbose_name_plural = "OBV Index Stock"

