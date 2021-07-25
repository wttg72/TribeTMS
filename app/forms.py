from django import forms
from datetime import datetime

class AvailabilityFrom(forms.Form):
    BIKE_CATEGORIES=(
        ('CUB','Underbone'),
        ('SPO','Sport'),
        ('STR','Street'),
        ('SCO','Scooter'),
    )

    bike_category = forms.ChoiceField(choices=BIKE_CATEGORIES, required=True)
    check_in = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M",] )
    check_out = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M",] )