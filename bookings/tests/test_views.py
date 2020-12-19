# from datetime import date
# from django.urls import reverse
# from django.test import TestCase
# from rest_framework.test import APITestCase
# from rest_framework import status
# from authentication.tests.factories import UserFactory
# from trips.tests.bus_factories import BusFactory, TripFactory
# from bookings.tests.factories import BookingFactory
# from trips.models import Bus
# from trips.serializers import BusSerializer


# class TestTripBookingEndpoint(APITestCase):

#     def _auth_header(self, token):
#         return f'Bearer {token}'

#     def _login(self, data):
#         url = reverse('auth:login')
#         return self.client.post(url, data, format='json')

#     def _create_bus(self, data, auth):
#         url = reverse("trips:bus")
#         return self.client.post(url, data, format="json", HTTP_AUTHORIZATION=auth)

#     def setUp(self):
#         password = 'password'
#         self.admin = UserFactory(
#             is_admin=True,
#             email='admin@test.com',
#             password=password,
#             first_name='admin',
#             last_name='brt',
#             is_staff=True
#         )
#         self.user = UserFactory(
#             email='user@test.com',
#             password=password,
#             first_name='nonny',
#             last_name='amadi',
#             is_admin=False
#         )

#         admin_token = self._login(
#             dict(email=self.admin.email, password=password)).data['data']['token']

#         self._admin_header = self._auth_header(admin_token)

#         token = self._login(
#             dict(email=self.user.email, password=password)).data['data']['token']

#         self._header = self._auth_header(token)

#         self._bus_data = {
#             "number_plate": "LAMBA",
#             "manufacturer": "Toyota",
#             "model": "Hiace",
#             "year": "2020",
#             "capacity": 20
#         }
#         self._bus_data_ = {
#             "number_plate": "BARN",
#             "manufacturer": "Toyota",
#             "model": "Hiace",
#             "year": "2020",
#             "capacity": 20
#         }
#         self.bus = self._create_bus(self._bus_data, self._admin_header).data

#         self._bus_data_two = {
#             "number_plate": "BBANAHAJ",
#             "manufacturer": "Honda",
#             "model": "Pilot",
#             "year": "2010",
#             "capacity": 18
#         }

#         self.buses = BusFactory(**self._bus_data_)
#         self.bus_two = BusFactory(**self._bus_data_two)

#         self._trip_data = {
#             "bus_id": self.bus_two.id,
#             "origin": "ikotun",
#             "destination": "ikeja",
#             "trip_date": date.today(),
#             "fare": 100.00,
#             "status": "active"
#         }
#         self._trip_full_capacity = {
#             "bus_id": self.bus_two.id,
#             "origin": "ikotun",
#             "destination": "ikeja",
#             "trip_date": date.today(),
#             "fare": 100.00,
#             "status": "active",
#             "curr_bus_capacity": 18
#         }
#         self.trip_ = TripFactory(**self._trip_data)
#         self.full_trip = TripFactory(**self._trip_full_capacity)
#         self.booking_data = {
#             "bus_id": self.buses.id,
#             "trip_id": self.trip_,
#             "user_id": self.user
#         }

#         self.booking_full = {
#             "bus_id": self.buses,
#             "trip_id": self.full_trip,
#             "user_id": self.user
#         }
#         self.bookings = BookingFactory(**self.booking_data)

#     def test_book_a_trip(self):
#         url = '/api/v1/bookings'
#         response = self.client.post(
#             url, HTTP_AUTHORIZATION=self._header, data=self.booking_data, format="json")
#         print(response.data)
#         self.assertEqual(True, True)
