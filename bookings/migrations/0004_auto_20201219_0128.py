# Generated by Django 3.1.4 on 2020-12-19 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_auto_20201219_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_number',
            field=models.CharField(default='BRT-4YkFF90Q9btC', max_length=155),
        ),
    ]
