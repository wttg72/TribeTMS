from django.http import request
from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, FormView, View
from django.urls import reverse, reverse_lazy
from .models import Bike, Booking
from .forms import AvailabilityFrom
from app.booking_functions.availability import check_availability

# Create your views here.

def BikeListView(request):
    bike = Bike.objects.all()[0]
    bike_categories = dict(bike.BIKE_CATEGORIES)
    bike_values = bike_categories.values()
    bike_list=[]
    for bike_category in bike_categories:
        bike = bike_categories.get(bike_category)
        bike_url = reverse('app:BikeDetailView', kwargs={
                            'category': bike_category})
        bike_list.append((bike,bike_url))

    context={
        "bike_list": bike_list,
    }

    return render(request, 'bike_list_view.html', context)

class BookingList(ListView):
    model = Booking
    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            booking_list = Booking.objects.all()
            return booking_list
        else:
            booking_list = Booking.objects.filter(user=self.request.user)
            return booking_list

class BikeDetailView(View):
    def get(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        form = AvailabilityFrom()
        bike_list = Bike.objects.filter(category=category)

        if len(bike_list) > 0:
            bike = bike_list[0]
            bike_category = dict(bike.BIKE_CATEGORIES).get(bike.category, None)
            context={
                'bike_category': bike_category,
                'form': form,
            }
            return render(request, 'bike_detail_view.html', context)
        else:
            return HttpResponse('Category does not exist.')

    def post(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        bike_list = Bike.objects.filter(category=category)
        form =  AvailabilityFrom(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            
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
