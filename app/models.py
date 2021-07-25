from django.db import models

# Create your models here.

class Bike(models.Model):
    BIKE_CATEGORIES=(
        ('CUB','Underbone'),
        ('SPO','Sport'),
        ('STR','Street'),
    )
    number = models.IntegerField()
    category = models.CharField(max_length=3, choices=BIKE_CATEGORIES)
