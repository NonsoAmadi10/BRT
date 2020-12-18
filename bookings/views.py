from django.shortcuts import render
from bookings.mixins import BookingViewSet
from datetime import datetime, timedelta, date
from django.shortcuts import get_object_or_404
from .serializers import BookingSerializer
from bookings.models import Booking
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from BRT.response import success_response, failure_response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from trips.utils import convert_date
# Create your views here.


class Booking(BookingViewSet):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated, ]
    query_set = Booking.objects.all()

    def create(self, *args, **kwargs):
        """ Creates Trip Bookings for all users who use this platform"""

        data = request.data
        trip_data = get_object_or_404(Booking, pk=data['trip_id'])
        if trip_data:
            serializer = self.serializer_class(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return success_response(serializer.data, 'Your Trip has been booked', status.HTTP_201_CREATED)
        else:
            return failure_response({}, 'trip id specified does  not exist', status.HTTP_400_BAD_REQUEST)
