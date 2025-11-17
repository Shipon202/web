from django import forms
from hotel.models import HotelStore

class HotelFrom(forms.ModelForm):
    class Meta:
        model = HotelStore
        fields = ['id', 'hotel_name', 'owner_name']
