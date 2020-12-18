from datetime import datetime
import os

from rest_framework import serializers
from django.contrib.auth import authenticate

from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    """Serializes registration requests and creates a new user."""

    # Ensure passwords are at least 8 characters long, no longer than 128
    # characters, and can not be read by the client.
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    is_admin = serializers.BooleanField(write_only=True)

    email = serializers.EmailField(max_length=255, write_only=True)

    #pylint: disable=missing-docstring

    class Meta:

        model = User
        fields = ['email', 'password', 'first_name',
                  'last_name', 'is_admin']

    def create(self, validated_data):
        """Creates a user"""
        if validated_data['is_admin']:
            validated_data['is_staff'] = True
            admin_user = User.objects.create_superuser(**validated_data)
            return admin_user
        else:
            new_user = User.objects.create_user(**validated_data)
            return {
                "first_name": new_user.first_name,
                "last_name": new_user.last_name,
                "email": new_user.email,
                "is_admin": new_user.is_admin
            }


class LoginSerializer(serializers.ModelSerializer):
    """Serializes a User Login"""

    email = serializers.EmailField(max_length=255)
    # Ensure passwords are at least 8 characters long, no longer than 128
    # characters, and can not be read by the client.
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    # The client should not be able to send a token along with a registration
    # request. Making `token` read-only handles that for us.
    token = serializers.CharField(max_length=255, read_only=True)
    is_admin = serializers.BooleanField(read_only=True)
    first_name = serializers.CharField(max_length=255, read_only=True)
    last_name = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        # List all of the fields that could possibly be included in a request
        # or response, including fields specified explicitly above.
        fields = ['email', 'password', 'token',
                  'first_name', 'last_name', 'email', 'is_admin']

    def validate(self, data):
        # The `validate` method is where we make sure that the current
        # instance of `LoginSerializer` has "valid". In the case of logging a
        # user in, this means validating that they've provided an email
        # and password and that this combination matches one of the users in
        # our database.
        email = data.get('email', None)
        password = data.get('password', None)

        # As mentioned above, an email is required. Raise an exception if an
        # email is not provided.
        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )

        # As mentioned above, a password is required. Raise an exception if a
        # password is not provided.
        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        # The `authenticate` method is provided by Django and handles checking
        # for a user that matches this email/password combination. Notice how
        # we pass `email` as the `username` value. Remember that, in our User
        # model, we set `USERNAME_FIELD` as `email`.
        user = authenticate(username=email, password=password)

        # If no user was found matching this email/password combination then
        # `authenticate` will return `None`. Raise an exception in this case.
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )

        # Django provides a flag on our `User` model called `is_active`. The
        # purpose of this flag to tell us whether the user has been banned
        # or otherwise deactivated. This will almost never be the case, but
        # it is worth checking for. Raise an exception in this case.
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        # The `validate` method should return a dictionary of validated data.
        # This is the data that is passed to the `create` and `update` methods
        # that we will see later on.
        return {
            'first_name': user.first_name,
            'email': user.email,
            'last_name': user.last_name,
            'is_admin': user.is_admin,
            'token': user.token
        }


class UserListQuerySerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    # Ensure passwords are at least 8 characters long, no longer than 128
    # characters, and can not be read by the client.
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
