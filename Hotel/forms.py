from django import forms
from . import models


class HotelForm(forms.ModelForm):
    class Meta:
        model = models.Hotel
        fields = '__all__'
