from django.urls import path, include

from .views import BusListViews, TripsViews
from rest_framework.routers import DefaultRouter

app_name = 'trips'

router = DefaultRouter()
router.register(r'', TripsViews, basename='trips')
urlpatterns = [
    path('bus', BusListViews.as_view(), name="bus"),
    path('', include(router.urls))

]
