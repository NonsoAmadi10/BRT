from django.conf.urls import url

from .views import BusListViews

app_name = 'trips'
urlpatterns = [
    url(r'bus', BusListViews.as_view(), name="bus"),
]
