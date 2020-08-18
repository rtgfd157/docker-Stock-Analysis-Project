from django.db import models


class ComapnyStockData(models.Model):
    """
    data about ticker, company, exchange market.
    """
    ticker = models.CharField(blank=False, null=False,
                              max_length=20, verbose_name="Ticker Name")

    company_name = models.CharField(
        blank=False, null=False, max_length=150, verbose_name="Company Name")

    stock_exchange = models.CharField(
        blank=False, null=False, max_length=20, verbose_name="Stock Exchange")
    
    update_time = models.DateField('update_time', auto_now=True)

    def __str__(self):
        return self.ticker + " " + self.company_name + " " + self.stock_exchange



class StockDayData(models.Model):
    """
        Day specific stock data -  planned to be 10 instances in db for each company stock.
    """

    company_stock_data = models.ForeignKey(ComapnyStockData, on_delete=models.CASCADE, related_name="company_by")

    close = models.DecimalField(
        blank=False, null=False, max_digits=10, decimal_places=3,  verbose_name="Close Price")

    volume = models.IntegerField(db_index=True,
        blank=False, null=False, verbose_name="Close Volume")

    stock_date = models.DateField('stock_date')

    def __str__(self):
        return str(self.company_stock_data) + " " + str(self.close) + " " + str(self.volume) + " " + str(self.stock_date)


    class Meta:
        constraints = [
        models.UniqueConstraint(fields=['company_stock_data', 'stock_date'], name='unique StockDayData')
    ]
