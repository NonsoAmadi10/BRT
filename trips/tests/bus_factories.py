import factory
from factory.django import DjangoModelFactory
from trips.models import Bus, Trip


class BusFactory(DjangoModelFactory):
    class Meta:
        model = Bus


class TripFactory(DjangoModelFactory):

    class Meta:
        model = Trip
