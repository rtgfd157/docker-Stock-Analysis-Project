# Generated by Django 3.1b1 on 2020-07-14 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_app', '0004_auto_20200714_1111'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='stockdaydata',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='stockdaydata',
            constraint=models.UniqueConstraint(fields=('company_stock_data', 'stock_date'), name='unique StockDayData'),
        ),
    ]
