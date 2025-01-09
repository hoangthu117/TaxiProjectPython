from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['car_type', 'pickup_location', 'dropoff_location', 'pickup_date', 'full_name', 'phone_number']