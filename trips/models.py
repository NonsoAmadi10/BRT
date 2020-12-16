from django.db import models

# Create your models here.


class Bus(models.Model):
    number_plate = models.CharField(db_index=True, max_length=12, unique=True)
    manufacturer = models.CharField(max_length=255, blank=False)
    year = models.CharField(blank=False, max_length=4)
    capacity = models.IntegerField(default=18)
    model = models.CharField(max_length=100)
    curr_capacity = models.IntegerField(default=0)

    def __str__(self):
        return self.number_plate

    class Meta:
        ordering = ['-capacity']


class Trip(models.Model):
    bus_id = models.ForeignKey(
        Bus, related_name='bus', on_delete=models.CASCADE)
    origin = models.CharField(max_length=255, blank=False, null=False)
    destination = models.CharField(max_length=255, blank=False, null=False)
    trip_date = models.DateField()
    fare = models.FloatField(default=0.0)
