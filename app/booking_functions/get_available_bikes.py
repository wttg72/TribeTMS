from app.models import Bike
from .availability import check_availability

def get_available_bikes(model, check_in, check_out):
    bike_list = Bike.objects.filter(model=model)
        
    available_bikes=[]

    for bike in bike_list:
        if check_availability(bike, check_in, check_out):
            available_bikes.append(bike)

    if len(available_bikes) > 0:
        return available_bikes
    else:
        return None