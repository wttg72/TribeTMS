from django.urls import path
from .views import BikeList, BookingList, BookingView

app_name='app'

urlpatterns= [
    path('bike_list/', BikeList.as_view(), name='BikeList'),
    path('booking_list/', BookingList.as_view(), name='BookingList'),
    path('book/', BookingView.as_view(), name='BookingView')
]