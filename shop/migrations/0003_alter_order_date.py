# Generated by Django 4.2.14 on 2024-07-25 14:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_order_date_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 7, 25, 18, 23, 24, 141438)),
        ),
    ]