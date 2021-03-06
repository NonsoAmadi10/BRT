# Generated by Django 3.1.4 on 2020-12-16 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_plate', models.CharField(db_index=True, max_length=12, unique=True)),
                ('manufacturer', models.CharField(max_length=255)),
                ('year', models.CharField(max_length=4)),
                ('capacity', models.IntegerField(max_length=2)),
                ('model', models.CharField(max_length=100)),
                ('curr_capacity', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-capacity'],
            },
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=255)),
                ('destination', models.CharField(max_length=255)),
                ('trip_date', models.DateField()),
                ('fare', models.FloatField(default=0.0)),
                ('bus_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bus', to='trips.bus')),
            ],
        ),
    ]
