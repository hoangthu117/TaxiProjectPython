from django.contrib import admin
from .models import Booking
admin.site.site_header = "Booking Admin"
admin.site.site_title = "Site Admin"
admin.site.index_title = "Welcome to Booking Admin Panel"
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'car_type', 'pickup_location', 'dropoff_location', 'pickup_date', 'phone_number')
    search_fields = ('full_name', 'car_type', 'pickup_location', 'dropoff_location')
    list_filter = ('car_type', 'pickup_date')