from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests
import time
# Create your views here.
def index (request):
    return render(request,'index.html')
def index_submit(request):
    if request.GET:
        city=request.GET['city']
    # PEGUE SUA API KEY NO SITE 
    url='http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&lang=pt&appid={ sua api key}'.format(city)
    res=requests.get(url).json()
    try:
        context={
            'cidade':res['name'],
            'pais':res['sys']['country'],
            'temperatura':res['main']['temp'],
            'descricao':res['weather'][0]['description'],
        }
    except:
        return HttpResponse('<h1><center>COLOQUE UMA CIDADE VALIDA <br> WRONG CITY TRY AGAIN </h1></center>')
    return render(request,'tempocity.html',context)