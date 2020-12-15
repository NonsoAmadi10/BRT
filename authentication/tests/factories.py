""" Reference for using factories:  https://adriennedomingus.com/blog/using-factoryboy-with-django-tests """
import factory
import random
from factory.django import DjangoModelFactory
from authentication.models import User


class UserFactory(DjangoModelFactory):

    email = factory.Sequence(lambda n: 'person{0}@test.com'.format(n))

    password = factory.PostGeneration(
        lambda user, create, extracted: user.set_password(extracted))

    class Meta:
        model = User
