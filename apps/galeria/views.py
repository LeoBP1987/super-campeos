from django.shortcuts import render
from django.http import HttpResponse
from apps.galeria.models import Categorias, Campeonatos, Times

def index(request):
    times = Times.objects.order_by('-data_registro').filter(publicado=True)
    return render(request,'index.html', {'cards':times})

def time(request, time_id):
    time = Times.objects.get(id=time_id)
    return render(request, 'time.html', {'time':time})