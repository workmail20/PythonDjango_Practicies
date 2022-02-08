import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext

def home(request):
    return render(request, 'home.html', {"CONST": '1111'})


def success(request):
    return render(request, 'success.html', {"CONST": '2222'})


def getWeather(request):
    client_ip = request.META['REMOTE_ADDR']
    return render(request, 'getWeather.html', {"client_ip": client_ip})


def showWeather(request):
    client_ip = request.META['REMOTE_ADDR']
    city = request.POST.get("cityWeather", "")
    countryInfo = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=c834c8344b09864e71783170a615d0fe').text
    return render(request, 'showWeather.html', {"client_ip": client_ip, "countryInfo": countryInfo})
