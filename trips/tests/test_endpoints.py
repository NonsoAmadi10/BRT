from datetime import date
from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from authentication.tests.factories import UserFactory
from trips.tests.bus_factories import BusFactory, TripFactory
from trips.models import Bus
from trips.serializers import BusSerializer


class TestBusEndpoint(APITestCase):

    def _auth_header(self, token):
        return f'Bearer {token}'

    def _login(self, data):
        url = reverse('auth:login')
        return self.client.post(url, data, format='json')

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

    def test_create_bus_with_admin_roles(self):
        url = reverse("trips:bus")
        response = self.client.post(
            url, data=self._bus_data_three, format="json", HTTP_AUTHORIZATION=self._admin_header)
        response_data = response.data
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        assert 'id' in response_data

    def test_create_bus_without_admin_roles(self):
        url = reverse("trips:bus")
        response = self.client.post(
            url, data=self._bus_data_three, format="json", HTTP_AUTHORIZATION=self._header)
        response_data = response.data
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(
            response_data['detail'], 'You do not have permission to perform this action.')

    def test_get_bus_data_with_admin_roles(self):
        url = reverse("trips:bus")
        response = self.client.get(
            url, HTTP_AUTHORIZATION=self._admin_header)
        response_data = response.data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response_data[0]['number_plate'], self._bus_data_two['number_plate'])

    def test_get_bus_data_without_admin_roles(self):
        url = reverse("trips:bus")
        response = self.client.get(
            url, HTTP_AUTHORIZATION=self._header)
        response_data = response.data

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(
            response_data['detail'], 'You do not have permission to perform this action.')
