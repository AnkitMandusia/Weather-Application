# home/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('weather/store', views.store_weather, name='store_weather'),
    path('weather/history/', views.weather_history, name='weather_history'),
]
