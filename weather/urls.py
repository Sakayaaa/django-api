from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home')
    path('current-weather/', views.CurrentWeather.as_view(), name='current_weather'),
]
