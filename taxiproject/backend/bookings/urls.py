# filepath: /c:/THUHH/DemoPythonWeb/taxiproject/backend/bookings/urls.py
from django.urls import path
from .views import booking_api_view

urlpatterns = [
    path('book/', booking_api_view, name='booking_api'),
]