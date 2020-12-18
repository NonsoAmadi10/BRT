from trips.models import Bus, Trip
from trips.serializers import TripSerializer, BusSerializer
from .models import Booking
from rest_framework import serializers


class BookingSerializer(serializers.ModelSerializer):
    trip_id = serializers.IntegerField()
    trips = TripSerializer(read_only=True)
    bus = BusSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = ['booking_number', 'user_id' 'trip_id', 'trips', 'bus']
        read_only_fields = ('created_at', 'booking_number')

    def create(self, validate_data):
        user = self.context['request'].user
        # Check if trip exists
        get_trip = Trip.objects.get(
            pk=validate_data['trip_id']).select_related('bus')
        book_trip = Booking.objects.create(user_id=user, trip_id=get_trip)
        return book_trip.select_related('owner', 'trip')
