import factory
from factory.django import DjangoModelFactory
from trips.models import Bus


class BusFactory(DjangoModelFactory):
    class Meta:
        model = Bus
