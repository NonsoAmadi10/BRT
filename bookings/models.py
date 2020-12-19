from django.db import models
from django.conf import settings
from bookings.utils import generate_booking_number
from django.shortcuts import get_object_or_404
from trips.models import Trip, Bus
# Create your models here.


class Booking(models.Model):
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='owner', on_delete=models.CASCADE)
    trip_id = models.OneToOneField(
        'trips.Trip', related_name='trip', on_delete=models.CASCADE)
    bus_id = models.ForeignKey(
        Bus, related_name='ride', on_delete=models.CASCADE)
    #seat_number = models.IntegerField()
    booking_number = models.CharField(
        max_length=155, default=generate_booking_number())
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=True)

    def __str__(self):
        return self.booking_number

    class Meta:
        db_table = 'bookings'
        ordering = ['-created_at']
