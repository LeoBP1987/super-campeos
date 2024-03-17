from django.contrib import admin
from django.urls import path
from apps.galeria.views import index, time

urlpatterns = [
    path('', index, name='index'),
    path('time/<int:time_id>', time, name='time')
]