from .models import Bus, Trip
from rest_framework.serializers import ModelSerializer


class BusSerializer(ModelSerializer):
    class Meta:
        model = Bus
        fields = '__all__'


class TripSerializer(ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'
        read_only_fields = ('curr_bus_capacity', 'id')
