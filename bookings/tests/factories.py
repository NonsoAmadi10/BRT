import factory
from factory.django import DjangoModelFactory
from bookings.models import Booking


class BookingFactory(DjangoModelFactory):
    class Meta:
        model = Booking
