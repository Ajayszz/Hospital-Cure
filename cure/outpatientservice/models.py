from tkinter.constants import CASCADE

from django.conf.global_settings import CACHES
from django.db import models

# Create your models here.

class Service(models.Model):
    category=models.CharField(max_length=250)
    fee=models.DecimalField(max_digits=5,decimal_places=2)
    category_pic=models.CharField(max_length=10000)

    def __str__(self):
        return self.category

class Doctor(models.Model):
    service=models.ForeignKey(Service,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    qualification=models.CharField(max_length=200)
    experience=models.CharField(max_length=100)
    doc_pic=models.CharField(max_length=100000)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient_name=models.CharField(max_length=250)
    patient_age=models.IntegerField()
    appointment_time=models.DateTimeField(auto_now=False)


    def __str__(self):
        return self.patient_name