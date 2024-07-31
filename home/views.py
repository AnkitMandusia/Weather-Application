from django.shortcuts import render, HttpResponse
import requests
from datetime import datetime, timezone, timedelta
import json

# Create your views here.

def index(request):
    if request.method == "POST":
        city = str(request.POST.get('city'))

        # Enter your "openweathermap.org" API_KEY below
        api_key = "da7959d94247c1cb80af6d42f6f0cc10"
        
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        data = requests.get(url).json()

        try:
            if data['cod'] == '404':
                return HttpResponse('{"status": "notfound"}')
            else:
                city_name = data['name']
                country = data.get('sys').get('country', '-')
                ts = data['dt']
                tzone = data['timezone']
                date_time = datetime.fromtimestamp(ts, tz=timezone(timedelta(seconds=tzone))).strftime('%Y-%m-%d')
                temp = int(data['main']['temp'])
                temp_F = format((temp*1.8)+32, '.1f')
                description = data['weather'][0]['description']
                humidity = data['main']['humidity']
                feels_like = int(data['main']['feels_like'])
                wind = format(data['wind']['speed']*3.6, '.1f')
                visibility = format(data['visibility']/1000, '.2f') 

                context = {'status': 'success', 'city': city_name, 'country': country, 'date_time':date_time, 'temp': temp, 'temp_F': temp_F, 'description': description, 'humidity': humidity, 'feels_like': feels_like, 'wind': wind, 'visibility': visibility}
                return HttpResponse(json.dumps(context))
        except:
            return HttpResponse('{"status": "error"}')
            

    return render(request, 'index.html')

# weather/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import WeatherHistory
import requests

def store_weather(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = "da7959d94247c1cb80af6d42f6f0cc10"
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric')
        data = response.json()
        
        if response.status_code == 200 and 'main' in data and 'weather' in data:
            weather_history = WeatherHistory(
                city=city,
                temperature=data['main']['temp'],
                description=data['weather'][0]['description'],
                timestamp=datetime.now()
            )
            weather_history.save()
            return render(request, 'weather/store_weather.html', {'message': 'Weather data stored successfully'})
        else:
            return render(request, 'weather/store_weather.html', {'message': 'Failed to retrieve weather data'})
    
    return render(request, 'weather/store_weather.html')

def weather_history(request):
    if request.method == 'GET':
        city = request.GET.get('city')
        if city:
            history = WeatherHistory.objects.filter(city=city).order_by('-timestamp')
            history_data = [
                {
                    'temperature': record.temperature,
                    'description': record.description,
                    'timestamp': record.timestamp
                }
                for record in history
            ]
            return render(request, 'weather/weather_history.html', {'city': city, 'history': history_data})
        else:
            return render(request, 'weather/weather_history.html', {'message': 'City not provided'})
    
    return render(request, 'weather/weather_history.html')