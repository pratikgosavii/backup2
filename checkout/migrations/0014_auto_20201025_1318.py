# Generated by Django 3.0.2 on 2020-10-25 07:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('checkout', '0013_auto_20201025_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placedorder_book',
            name='buyer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='product_buyer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user_address_detail',
            name='buyer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='buyer_product', to=settings.AUTH_USER_MODEL),
        ),
    ]
