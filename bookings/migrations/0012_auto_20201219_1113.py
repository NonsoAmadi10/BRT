# Generated by Django 3.1.4 on 2020-12-19 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0011_auto_20201219_0227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_number',
            field=models.CharField(default='BRT-Wb3SmDleuPme', max_length=155),
        ),
    ]