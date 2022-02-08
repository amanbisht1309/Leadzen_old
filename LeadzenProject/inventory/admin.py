from django.contrib import admin

# Register your models here.
from .models import vehicle_type,Customer,Rentals

admin.site.register(vehicle_type)
admin.site.register(Customer)
admin.site.register(Rentals)