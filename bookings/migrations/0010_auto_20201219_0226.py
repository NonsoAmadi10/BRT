# Generated by Django 3.1.4 on 2020-12-19 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0009_auto_20201219_0226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_number',
            field=models.CharField(default='BRT-3wBfoAvXgQjv', max_length=155),
        ),
    ]