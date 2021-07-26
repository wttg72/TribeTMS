from django.urls import path
from .views import BikeListView, BookingListView, BikeDetailView, CancelBookingView

app_name='app'

urlpatterns= [
    path('bike_list/', BikeListView, name='BikeListView'),
    path('booking_list/', BookingListView.as_view(), name='BookingListView'),
    path('bike/<category>', BikeDetailView.as_view(), name='BikeDetailView'),
    path('booking/cancel/<pk>', CancelBookingView.as_view(), name='CancelBookingView')
]