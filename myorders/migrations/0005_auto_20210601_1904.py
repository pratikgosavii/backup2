# Generated by Django 3.0.2 on 2021-06-01 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myorders', '0004_auto_20210601_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placedorder_book',
            name='order_status',
            field=models.IntegerField(choices=[(1, 'order cancled'), (2, 'complaint raise'), (3, 'raise return'), (4, 'return in progress'), (5, 'return accepted'), (6, 'return pickedup'), (7, 'return order recevied'), (8, 'return product quality check in progress'), (9, 'return payment in progress'), (10, 'return payment complete'), (11, 'order is open'), (12, 'order is accepted'), (13, 'order packing'), (14, 'out for delivery'), (15, 'delivered')], default='order is open'),
        ),
    ]
