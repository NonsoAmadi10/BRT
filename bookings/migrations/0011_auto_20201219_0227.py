# Generated by Django 3.1.4 on 2020-12-19 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0010_auto_20201219_0226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='bus',
            new_name='bus_id',
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_number',
            field=models.CharField(default='BRT-FI238f2VewAb', max_length=155),
        ),
    ]