from django.shortcuts import render
from django.db.utils import IntegrityError
from datetime import datetime, timedelta, date
from django.shortcuts import get_object_or_404
from .serializers import BookingSerializer
from bookings.models import Booking
from trips.models import Trip, Bus
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, viewsets
from BRT.response import success_response, failure_response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from trips.utils import convert_date
# Create your views here.


class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated, ]
    query_set = Booking.objects.select_related('owner', 'trips', 'ride')

    def create(self, request, *args, **kwargs):
        """ Creates Trip Bookings for all users who use this platform"""

        data = request.data

        try:
            trip_data = get_object_or_404(Trip, pk=data['trip_detail'])

            if trip_data:
                if trip_data.curr_bus_capacity == trip_data.bus_id.capacity:
                    return failure_response({}, 'Bus capacity is full', status.HTTP_409_CONFLICT)
                else:
                    data['user_id'] = request.user
                    data['bus_id'] = trip_data.bus_id
                    serializer = self.serializer_class(
                        data=data, context={'user': request.user})
                    serializer.is_valid(raise_exception=True)
                    trip_data.curr_bus_capacity += 1
                    trip_data.save()
                    serializer.save()
                    return success_response(serializer.data, 'Your Trip has been booked', status.HTTP_201_CREATED)
            else:
                return failure_response({}, 'trip id specified does  not exist', status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            return failure_response({}, 'You have made this booking before', status.HTTP_409_CONFLICT)
