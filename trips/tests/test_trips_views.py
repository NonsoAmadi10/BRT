from datetime import date
from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from authentication.tests.factories import UserFactory
from trips.tests.bus_factories import BusFactory, TripFactory
from trips.models import Bus
from trips.serializers import BusSerializer


class TestTripBusEndpoint(APITestCase):

    def _auth_header(self, token):
        return f'Bearer {token}'

    def _login(self, data):
        url = reverse('auth:login')
        return self.client.post(url, data, format='json')

    def _create_bus(self, data, auth):
        url = reverse("trips:bus")
        return self.client.post(url, data, format="json", HTTP_AUTHORIZATION=auth)

    def setUp(self):
        password = 'password'
        self.admin = UserFactory(
            is_admin=True,
            email='admin@test.com',
            password=password,
            first_name='admin',
            last_name='brt',
            is_staff=True
        )
        self.user = UserFactory(
            email='user@test.com',
            password=password,
            first_name='nonny',
            last_name='amadi',
            is_admin=False
        )

        admin_token = self._login(
            dict(email=self.admin.email, password=password)).data['data']['token']

        self._admin_header = self._auth_header(admin_token)

        token = self._login(
            dict(email=self.user.email, password=password)).data['data']['token']

        self._header = self._auth_header(token)

        self._bus_data = {
            "number_plate": "EMX5000M",
            "manufacturer": "Toyota",
            "model": "Hiace",
            "year": "2020",
            "capacity": 20
        }
        self.bus = self._create_bus(self._bus_data, self._admin_header).data

        self._bus_data_two = {
            "number_plate": "AJM120P",
            "manufacturer": "Honda",
            "model": "Pilot",
            "year": "2010",
            "capacity": 18
        }

        self._bus_data_three = {
            "number_plate": "RMD120P",
            "manufacturer": "Honda",
            "model": "Pilot",
            "year": "2010",
            "capacity": 18
        }

        self.buses = BusFactory(**self._bus_data_two)

        self._trip_data = {
            "bus_id": self.buses,
            "origin": "ikotun",
            "destination": "ikeja",
            "trip_date": date.today(),
            "fare": 100.00,
            "status": "active"
        }
        self.trips = TripFactory(**self._trip_data)
        self._trip_data_two = {
            "bus_id": 1,
            "origin": "ikeja",
            "destination": "ikotun",
            "trip_date": date.today(),
            "fare": 100.00,
            "status": "active"
        }
        self._incorrect_date_data = {
            "bus_id": 1,
            "origin": "ikeja",
            "destination": "ikotun",
            "trip_date": "12-10-2020",
            "fare": 200.00,
            "status": "active"
        }

    def test_create_trip_with_admin_roles(self):
        url = '/api/v1/trips/'
        response = self.client.post(
            url, HTTP_AUTHORIZATION=self._admin_header, data=self._trip_data_two, format="json")
        response_data = response.data
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        assert response_data['status'].startswith('Success')
        self.assertEqual(response_data['data']['destination'], 'ikotun')

    def test_create_trip_with_out_admin_roles(self):
        url = '/api/v1/trips/'
        response = self.client.post(
            url, HTTP_AUTHORIZATION=self._header, data=self._trip_data_two, format="json")
        response_data = response.data
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(
            response_data['detail'], 'You do not have permission to perform this action.')

    def test_create_trip_incorrect_date(self):
        url = '/api/v1/trips/'
        response = self.client.post(
            url, HTTP_AUTHORIZATION=self._admin_header, data=self._incorrect_date_data, format="json")
        response_data = response.data
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response_data['error'], 'Incorrect data format, should be YYYY-MM-DD')

    def test_create_trip_incorrect_date(self):
        url = '/api/v1/trips/'
        self._incorrect_date_data['trip_date'] = '2020-12-02'
        response = self.client.post(
            url, HTTP_AUTHORIZATION=self._admin_header, data=self._incorrect_date_data, format="json")
        response_data = response.data
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response_data['error'], 'Trip date can only include today and beyond')

    def test_get_trip_data(self):
        url = '/api/v1/trips/'
        response = self.client.get(
            url, HTTP_AUTHORIZATION=self._header)
        response_data = response.data
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        assert len(response_data['data']) == 1
