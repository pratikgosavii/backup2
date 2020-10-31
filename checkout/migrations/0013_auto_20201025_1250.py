# Generated by Django 3.0.2 on 2020-10-25 07:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('checkout', '0012_auto_20201010_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placedorder_book',
            name='buyer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='product_buyer3434', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user_address_detail',
            name='buyer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='buyer_product344', to=settings.AUTH_USER_MODEL),
        ),
    ]