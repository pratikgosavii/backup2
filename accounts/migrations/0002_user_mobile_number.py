# Generated by Django 3.0.2 on 2021-05-20 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mobile_number',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
    ]
