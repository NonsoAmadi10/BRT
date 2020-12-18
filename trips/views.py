from datetime import datetime, timedelta, date
from django.shortcuts import get_object_or_404
from .serializers import BusSerializer, TripSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from trips.messages.message import TRIP_ADDED, TRIP_UPDATED
from BRT.response import success_response, failure_response
from rest_framework.decorators import permission_classes
from .permissions import IsAdminOrReadOnly
from .models import Bus, Trip
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from trips.utils import convert_date
# Create your views here.


class BusListViews(ListCreateAPIView):
    """ Handles the registration and listing of buses available on the platform """

    serializer_class = BusSerializer
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        queryset = Bus.objects.all()
        return queryset


class TripsViews(ModelViewSet):
    """ Admin Users Create Bus Trips but Only Regular Users and Admin can view all available trips
    """

    serializer_class = TripSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def get_queryset(self):
        queryset = Trip.objects.all()
        return queryset

    @convert_date
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['bus_id', 'origin', 'destination',
                      'fare', 'trip_date', 'status'],
            properties={
                'bus_id': openapi.Schema(type=openapi.TYPE_INTEGER),
                'origin': openapi.Schema(type=openapi.TYPE_STRING),
                'destination': openapi.Schema(type=openapi.TYPE_STRING),
                'fare': openapi.Schema(type=openapi.TYPE_INTEGER),
                'status': openapi.Schema(type=openapi.TYPE_STRING),
                'trip_date': openapi.Schema(type=openapi.TYPE_STRING)

            },
        ),
        responses={201: TripSerializer(many=True)},
        tags=['Trips'],
    )
    def create(self, request, *args, **kwargs):
        """ Only admin Users can create a trip listing"""

        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return success_response(serializer.data, TRIP_ADDED, status.HTTP_201_CREATED)

    @swagger_auto_schema(responses={200: TripSerializer(many=True)})
    def list(self, request, *args, **kwargs):
        "returns all available trips for both admin and regular users"
        startdate = date.today()
        enddate = startdate + timedelta(days=6)
        print(enddate)
        response = Trip.objects.filter(trip_date__range=[startdate, enddate])
        serializer = self.serializer_class(response, many=True)
        return success_response(serializer.data, 'trips retrieved successfully', status.HTTP_200_OK)

    @convert_date
    def update(self, request, pk):
        """ Allows Admin users to update a trip"""

        _data = request.data

        trip = get_object_or_404(Trip.objects.all(), pk=pk)
        # Here is that serialize, validate, save pattern we talked about
        # before.
        serializer = self.serializer_class(
            trip, data=_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return success_response(serializer.data, TRIP_UPDATED, status.HTTP_200_OK)
