# Generated by Django 3.1b1 on 2020-07-14 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main_app', '0003_auto_20200713_1857'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='stockdaydata',
            unique_together={('company_stock_data', 'stock_date')},
        ),
    ]