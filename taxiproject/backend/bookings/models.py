from django.db import models

class Booking(models.Model):
    CAR_TYPE_CHOICES = [
        ('sedan', 'Sedan'),
        ('suv', 'SUV'),
        ('hatchback', 'Hatchback'),
    ]

    car_type = models.CharField(max_length=10, choices=CAR_TYPE_CHOICES)
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    pickup_date = models.DateField()
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.full_name} - {self.car_type}"