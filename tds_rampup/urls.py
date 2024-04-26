from django.urls import path
from .views import subscribers_api_list, subscriber_api_detail
from .views import locations_api_list, location_api_detail

app_name = 'rampup'

urlpatterns = [
    path(
        'subscribers/',
        subscribers_api_list,
        name='subscribers'
    ),
    path(
        'subscribers/<int:pk>/',
        subscriber_api_detail,
        name='subscriber_detail'
    ),
    path(
        'subscribers/<int:pk>/channel-lineup/',
        subscriber_api_detail,
        name='subscriber_detail_line_up'
    ),
    path(
        'locations/',
        locations_api_list,
        name='locations'
    ),
    path(
        'locations/<str:pk>/',
        location_api_detail,
        name='locations_detail'
    ),
]
