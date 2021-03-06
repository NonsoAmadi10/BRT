# Generated by Django 3.1.4 on 2020-12-19 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0004_trip_status'),
        ('bookings', '0008_auto_20201219_0202'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='bus',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='ride', to='trips.bus'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_number',
            field=models.CharField(default='BRT-CUNph102qZ63', max_length=155),
        ),
    ]
