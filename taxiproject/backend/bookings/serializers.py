from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['car_type', 'pickup_location', 'dropoff_location', 'pickup_date', 'full_name', 'phone_number']