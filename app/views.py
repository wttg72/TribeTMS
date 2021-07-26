from django.http import request
from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, FormView, View, DeleteView
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import DeleteView
from .models import Bike, Booking
from .forms import AvailabilityForm
from app.booking_functions.availability import check_availability
from app.booking_functions.get_bike_model_url_list import get_bike_model_url_list
from app.booking_functions.get_bike_info_human_format import get_bike_model_human_format
from app.booking_functions.get_available_bikes import get_available_bikes
from app.booking_functions.book_bike import book_bike

# Create your views here.

def BikeListView(request):
    bike_model_url_list =  get_bike_model_url_list()
    
    context={
        "bike_list": bike_model_url_list,
    }

    return render(request, 'bike_list_view.html', context)

class BookingListView(ListView):
    model = Booking
    template_name = "booking_list_view.html"
    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            booking_list = Booking.objects.all()
            return booking_list
        else:
            booking_list = Booking.objects.filter(user=self.request.user)
            return booking_list

class BikeDetailView(View):
    def get(self, request, *args, **kwargs):
        model = self.kwargs.get('model', None)
        bike_model_human_format = get_bike_model_human_format(model)
        form = AvailabilityForm()
        if bike_model_human_format is not None:
            context={
                'bike_model': bike_model_human_format,
                'form': form,
            }
            return render(request, 'bike_detail_view.html', context)
        else:
            return HttpResponse('Model does not exist.')

    def post(self, request, *args, **kwargs):
        model = self.kwargs.get('model', None)
        
        form =  AvailabilityForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

        available_bikes = get_available_bikes(model, data['check_in'], data['check_out'])

        if available_bikes is not None:
            booking = book_bike(request, available_bikes[0], data['check_in'], data['check_out'])
            return HttpResponse(booking)
        else:
            return HttpResponse("All of this model of bikes are booked for the dates you have requested! Please try another model or change the dates!")

class CancelBookingView(DeleteView):
    model = Booking
    template_name = 'booking_cancel_view.html'
    success_url = reverse_lazy('app:BookingListView')