from django.shortcuts import render, HttpResponse
from app.models import Bike

def get_bike_model_human_format(model):
    bike = Bike.objects.all()[0]
    bike_model = dict(bike.BIKE_MODELS).get(model, None)
    return bike_model