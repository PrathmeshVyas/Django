# Generated by Django 3.2.5 on 2021-11-18 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_rename_zipcode_orders_zip_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.CharField(default='', max_length=50),
        ),
    ]