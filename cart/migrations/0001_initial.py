# Generated by Django 3.0.2 on 2021-05-18 18:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='wishlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('buyer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='buyerwishlist', to=settings.AUTH_USER_MODEL)),
                ('product_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='bookswishlist', to='home.books')),
            ],
        ),
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('buyer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to=settings.AUTH_USER_MODEL)),
                ('product_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='home.books')),
            ],
        ),
    ]
