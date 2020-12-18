from django.urls import path, include

from .views import BookingViewSet
from rest_framework.routers import DefaultRouter

app_name = 'booking'

router = DefaultRouter()
router.register(r'', BookingViewSet, basename='book')
urlpatterns = [
    path('', include(router.urls))

]
