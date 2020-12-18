import json
from django.db import models

# Create your models here.


class Bus(models.Model):
    number_plate = models.CharField(db_index=True, max_length=12, unique=True)
    manufacturer = models.CharField(max_length=255, blank=False)
    year = models.CharField(blank=False, max_length=4)
    capacity = models.IntegerField(default=18)
    model = models.CharField(max_length=100, blank=False)

    def __repr__(self):
        return json.dumps(self.__dict__)

    class Meta:
        ordering = ['-capacity']


class Trip(models.Model):
    STATUS = (
        ('active', 'active'),
        ('cancelled', 'cancelled'),
        ('delayed', 'delayed')
    )
    bus_id = models.ForeignKey(
        'Bus', related_name='bus', on_delete=models.CASCADE)
    origin = models.CharField(max_length=255, blank=False, null=False)
    destination = models.CharField(max_length=255, blank=False, null=False)
    trip_date = models.DateField()
    status = models.CharField(default='active', max_length=20, choices=STATUS)
    fare = models.FloatField(default=0.0)
    curr_bus_capacity = models.IntegerField(default=0)

    def __str__(self):
        return f"""
        Dest: {self.origin} to {self.destination}\n
        Date: {self.trip_date}\n
        Fare: {self.fare}
        """

    @property
    def bus_full(self):
        return self.curr_bus_capacity == self.bus.capacity
