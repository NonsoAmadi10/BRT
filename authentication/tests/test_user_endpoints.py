from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework import status
from authentication.tests.factories import UserFactory
from authentication.models import User
from authentication.messages.success import USER_CREATED, LOGIN_SUCCESS


class TestUserEndpoint(APITestCase):

    def setUp(self):
        password = 'password'
        self.admin = UserFactory(
            is_admin=True,
            email='admin@test.com',
            password=password,
            first_name='admin',
            last_name='brt'
        )
        self.user = UserFactory(
            email='user@test.com',
            password=password,
            first_name='nonny',
            last_name='amadi',
            is_admin=False
        )

    def test_user_signup_with_valid_data_succeeds(self):
        url = reverse('auth:signup')
        data = {
            'email': 'user1@test.com',
            'password': 'password',
            'first_name': 'amadni',
            'last_name': 'jowo',
            'is_admin': False
        }

        response = self.client.post(url,
                                    data, format='json')
        response_data = response.data
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_data['message'], USER_CREATED)
        self.assertEqual(response_data['data']
                         ['first_name'], data['first_name'])
        self.assertEqual(response_data['status'], 'Success')
        assert len(User.objects.filter(
            email=data['email']).all()) == 1

    def test_user_signup_with_invalid_data_fail(self):
        url = reverse('auth:signup')
        data = {
            'email': 'user1@testcom',
            'password': 'password',
            'first_name': 'amadi',
            'last_name': 'jowo',
            'is_admin': False
        }

        response = self.client.post(url, data, format='json')

        response_data = response.data
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response_data['email'][0], 'Enter a valid email address.')

    def test_user_signup_with_incomplete_data_fails(self):
        url = reverse('auth:signup')
        data = {
            'email': 'user1@test.com',
            'first_name': 'new',
            'last_name': 'man',
            'is_admin': False
        }

        response = self.client.post(url,
                                    data, format='json')
        response_data = response.data
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response_data['password']
                         [0], 'This field is required.')

    def test_user_signin_with_valid_data_succeeds(self):
        url = reverse('auth:login')
        data = {
            'email': 'user@test.com',
            'password': 'password'
        }

        response = self.client.post(url, data, format='json')
        response_data = response.data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data['message'], LOGIN_SUCCESS)
        self.assertEqual(response_data['data']['email'], data['email'])
        assert 'token' in response_data['data']
        self.token = response_data['data']['token']

    def test_user_signin_not_found_fails(self):
        url = reverse('auth:login')
        data = {
            'email': 'user1@test.gmail',
            'password': 'password'
        }

        response = self.client.post(url,
                                    data, format='json')
        response_data = response.data
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response_data['error'][0], 'A user with this email and password was not found.')
