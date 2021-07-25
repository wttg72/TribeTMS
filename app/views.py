from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, FormView
from .models import Bike, Booking
from .forms import AvailabilityFrom
from app.booking_functions.availability import check_availability

# Create your views here.

class BikeList(ListView):
    model = Bike

class BookingList(ListView):
    model = Booking

class BookingView(FormView):
    form_class = AvailabilityFrom
    template_name = 'availability_form.html'

    def form_valid(self, form):
        data = form.cleaned_data
        bike_list = Bike.objects.filter(category=data['bike_category'])
        available_bikes=[]
        for bike in bike_list:
            if check_availability(bike, data['check_in'], data['check_out']):
                available_bikes.append(bike)

        if len(available_bikes) > 0:
            bike = available_bikes[0]
            booking = Booking.objects.create(
                user = self.request.user,
                bike=bike,
                check_in = data['check_in'],
                check_out = data['check_out']
            )
            booking.save()
            return HttpResponse(booking)
        
        else:
            return HttpResponse("All of this category of bikes are booked! Please try another category.")
