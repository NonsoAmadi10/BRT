from django.test import TestCase
from trips.models import Bus, Trip

from datetime import datetime


class BusesAndTripsTestCase(TestCase):
    def setUp(self):
        self._bus = Bus.objects.create(
            number_plate="EX85000", manufacturer="toyota", year="2020")

        self._trip = Trip.objects.create(bus_id=self._bus, origin="ikotun", destination="ikeja",
                                         trip_date=datetime.strptime('12-27-2020', '%m-%d-%Y').date(), fare=150.0)

    def test_bus_trip_model(self):
        self.assertEqual(self._bus.number_plate, "EX85000")
        self.assertEqual(self._trip.trip_date, datetime.strptime(
            '12-27-2020', '%m-%d-%Y').date())
        self.assertEqual(self._bus.year, "2020")
        self.assertEqual(self._trip.origin, "ikotun")
