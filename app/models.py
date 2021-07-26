from django.db import models
from django.conf import settings
from django.urls import reverse_lazy

# Create your models here.

class Bike(models.Model):
    BIKE_CATEGORIES=(
        ('CUB','Underbone'),
        ('SPO','Sport'),
        ('STR','Street'),
        ('SCO','Scooter'),
    )

    BIKE_CLASS=(
        ('2B','Class 2B'),
        ('2A','Class 2A'),
        ('2','Class 2'),
    )

    BIKE_MODELS=(
        ('Aerox','Yamaha Aerox 155'),
        ('Sniper','Yamaha Sniper T150'),
        ('FZ16','Yamaha FZ16'),
        ('FZ16ST','Yamaha FZ16ST'),
        ('CB190R','Honda CB190R'),
        ('CB400 Sp2','Honda CB400 (Super 4) Spec 2'),
        ('CB400 Sp3','Honda CB400 (Super 4) Spec 3'),
    )

    plate_no = models.CharField(max_length=8, null=True)
    category = models.CharField(max_length=3, choices=BIKE_CATEGORIES, null=True)
    bike_class = models.CharField(max_length=2, choices=BIKE_CLASS, null=True)
    model = models.CharField(max_length=12, choices=BIKE_MODELS, null=True)
    
    def __str__(self):
        return f'{self.model} ({self.plate_no}) [{self.bike_class} | {self.category}]'

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f'From: {self.check_in.strftime("%d-%b-%Y %H:%M")} To: {self.check_out.strftime("%d-%b-%Y %H:%M")}'

    def get_bike_model(self):
        bike_models = dict(self.bike.BIKE_MODELS)
        bike_model = bike_models.get(self.bike.model)
        return bike_model
    
    def get_bike_category(self):
        bike_categories = dict(self.bike.BIKE_CATEGORIES)
        bike_category = bike_categories.get(self.bike.category)
        return bike_category

    def get_cancel_booking_url(self):
        return reverse_lazy('app:CancelBookingView', args=[self.pk, ])