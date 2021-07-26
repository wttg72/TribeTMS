from django.urls import path
from .views import BikeListView, BookingList, BookingView, BikeDetailView

app_name='app'

urlpatterns= [
    path('bike_list/', BikeListView, name='BikeList'),
    path('booking_list/', BookingList.as_view(), name='BookingList'),
    path('book/', BookingView.as_view(), name='BookingView'),
    path('bike/<category>', BikeDetailView.as_view(), name='BikeDetailView')
]