from django.test import TestCase

from authentication.models import User
# Create your tests here.


class UserModelTestCase(TestCase):

    def setUp(self):
        User.objects.create(email="nonsoamadi@aol.com",
                            password="password")
        User.objects.create(email="davido@gmail.com",
                            password="DMW30BG")

    def test_users(self):
        nonso = User.objects.get(email="nonsoamadi@aol.com")
        david = User.objects.get(email="davido@gmail.com")

        self.assertEqual(david.is_active, True)
        self.assertEqual(david.is_active, True)
