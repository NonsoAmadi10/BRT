from django.test import TestCase
from trips.models import Bus, Trip

from authentication.models import User
from bookings.models import Booking
from datetime import datetime


class Bookings(TestCase):
    def setUp(self):
        self.user = User.objects.create(email="nonsoamadi@aol.com",
                                        password="password")
        self._bus = Bus.objects.create(
            number_plate="EX85000", manufacturer="toyota", year="2020")

        self._trip = Trip.objects.create(bus_id=self._bus, origin="ikotun", destination="ikeja",
                                         trip_date=datetime.strptime('12-27-2020', '%m-%d-%Y').date(), fare=150.0)
        self._booking = Booking.objects.create(
            user_id=self.user, trip_id=self._trip, bus_id=self._bus)

    def test_booking_model(self):
        self.assertEqual(self._booking.paid, True)
