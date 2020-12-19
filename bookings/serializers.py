from trips.models import Bus, Trip
from trips.serializers import TripSerializer, BusSerializer
from authentication.serializers import UserSerializer
from .models import Booking
from rest_framework import serializers


class BookingSerializer(serializers.ModelSerializer):
    user_id = UserSerializer(read_only=True)
    trip_detail = serializers.IntegerField(write_only=True)
    trip_id = TripSerializer(read_only=True)
    bus = BusSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = ['booking_number', 'user_id', 'trip_id', 'bus', 'trip_detail']
        read_only_fields = ('created_at', 'booking_number')

    def create(self, validate_data):
        user = self.context['user']
        # Check if trip exists
        get_trip = Trip.objects.get(
            pk=validate_data['trip_detail'])
        book_trip = Booking.objects.create(user_id=user, trip_id=get_trip)
        return book_trip
