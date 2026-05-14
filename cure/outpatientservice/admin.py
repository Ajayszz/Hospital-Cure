from django.contrib import admin
from .models import Service,Doctor,Appointment

# Register your models here.

admin.site.register(Service)
admin.site.register(Doctor)
admin.site.register(Appointment)
