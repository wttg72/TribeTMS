from django.db import models

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

    BIKE_NAME=(
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
    bike_model = models.CharField(max_length=12, choices=BIKE_NAME, null=True)
    
    def __str__(self):
        return f'{self.plate_no} {self.bike_class} {self.category} {self.bike_model}'
