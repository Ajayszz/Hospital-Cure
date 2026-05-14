from django.contrib import admin
from django.urls import path
from django.urls import include
from django.urls import re_path
from rest_framework.urls import app_name

from outpatientservice import views

app_name='outpatientservice'

urlpatterns = [
    re_path(r'^$',views.index,name='index'),
    re_path(r'book-appointment/', views.bookAppointment, name='book_appointment'),
    re_path(r'(?P<category_name>[^%s]*)/',views.serviceInfo,name='service_info')
]