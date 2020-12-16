from django.shortcuts import render
from .serializers import BusSerializer, TripSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import ListCreateAPIView
from .permissions import IsAdminOnly
from .models import Bus
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
# Create your views here.


class BusListViews(ListCreateAPIView):
    """ Handles the registration and listing of buses available on the platform """

    serializer_class = BusSerializer
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        queryset = Bus.objects.all()
        return queryset
