# Generated by Django 3.1.4 on 2020-12-17 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0003_auto_20201216_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='status',
            field=models.CharField(choices=[('active', 'active'), ('cancelled', 'cancelled'), ('delayed', 'delayed')], default='active', max_length=20),
        ),
    ]
