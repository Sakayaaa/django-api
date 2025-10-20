from django.shortcuts import render
import requests
from django.views import View


# def home(request):
#     url = 'https://api.openweathermap.org/data/2.5/weather'
#     appid = '6ad934a76186d5d2fb596a8e925a0cae'
#     q = 'Washington'
#     units = 'metric'

#     # response = requests.get(
#     #     url=url, params={'appid': appid, 'q': q, 'units': units}
#     #     ).json()
    
#     response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={q}&appid={appid}&units={units}").json()
    
#     city = response['name']
#     temp = response['main']['temp']
#     icon = response['weather'][0]['icon']

#     return render(request, 'weather/home.html', {'city': city, 'temp': temp, 'icon': icon})


class CurrentWeather(View):
    # Similar to 'if request.method == "POST" ' in FBV
    def post(self, request):
        pass
    
    # Similar to 'if request.method == "GET" ' in FBV
    def get(self, request):
        q = 'q'
        appid = '6ad934a76186d5d2fb596a8e925a0cae'
        units = 'units'

        url = f'https://api.openweathermap.org/data/2.5/weather?q={q}&appid={appid}&units={units}'
        res = requests.get()
        
        return render(request, 'weather/home.html', {})