from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.reverse import reverse

from outpatientservice.models import Service, Doctor, Appointment
from django.template import loader
# Create your views here.
import datetime
def index(request):
    all_services=Service.objects.all()
    all_doctors=Doctor.objects.all()
    context={
        'all_services':all_services,
        'all_doctors':all_doctors,
        'timestamp':datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

    }

    template=loader.get_template('outpatientservice/index.html')

    return HttpResponse(template.render(context,request))

def serviceInfo(request,category_name):
    service=Service.objects.get(category=category_name)
    context={'service':service}
    template=loader.get_template('outpatientservice/service_info.html')
    return HttpResponse(template.render(context,request))


def bookAppointment(request):
    new_app=Appointment()
    new_app.doctor=Doctor.objects.get(pk=request.POST.get('doctor_name'))
    new_app.appointment_time=request.POST.get('your_time')
    new_app.patient_name=request.POST.get('your_name')
    new_app.patient_age = request.POST.get('your_age')
    new_app.save()
    return HttpResponse(reverse('outpatientservice:index'))