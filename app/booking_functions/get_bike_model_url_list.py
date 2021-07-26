from app.models import Bike
from django.urls import reverse

def get_bike_model_url_list():
    bike = Bike.objects.all()[0]
    bike_models = dict(bike.BIKE_MODELS)

    bike_model_url_list=[]
    for model in bike_models:
        bike_model = bike_models.get(model)
        bike_url = reverse('app:BikeDetailView', kwargs={
                            'model': model})
        bike_model_url_list.append((bike_model,bike_url))
    return bike_model_url_list