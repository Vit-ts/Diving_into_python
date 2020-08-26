import pyowm
import os
import tempfile
import json

def get_predict(city):
    owm = pyowm.OWM('bfd3b5564fb9cebe25312293934202a5')
    print("sending HTTP request")
    observation = owm.weather_at_place(str(city))
    w = observation.get_weather()
    return w

class city_forecast:
    
    def __init__(self, name, fore_cast=None):
        self.name = name
        self.fore_cast = fore_cast
    
    def forecast(self, city):
        call = get_predict(city)
        forecast = {
            city : "-->",
            "temp" : call.get_temperature('celsius')['temp'],
            "wind" : call.get_wind()['speed'],
            "pressure" : call.get_pressure()['press'],
            "humidity" : call.get_humidity()
        }
        return forecast
        

def _main():
    while True:
        city_1 = city_forecast(input("Введите город, погоду которого вы желаете узнать: "))
        if city_1.name == "exit":
            print("Closed the city.py")
            break
        city_1.fore_cast = city_1.forecast(city_1.name)
        print(city_1.fore_cast)
        

if __name__ == "__main__":
    _main()