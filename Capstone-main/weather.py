import json
from pyowm.owm import OWM
import datetime
import os

class WeatherInfo:
    def __init__(self, City, Country, apiKey):
        self.city = City
        self.Country = Country
        # https://home.openweathermap.org/api_keys
        self.apiKey = apiKey
        self.owm = OWM(apiKey)
        self.mgr = self.owm.weather_manager()
        

    def get_weather_data(self):
        # Get the observation object for the City, Country
        obs = self.mgr.weather_at_place(f'{self.city}, {self.Country}')
        location = obs.location
        lat = location.lat
        lon = location.lon
        # Get weather forecast using onecall
        forecast = self.mgr.one_call(lat=lat, lon=lon)
        # Extract current weather data
        current_weather = forecast.current
        # Get humidity, temperature, and pressure
        clouds = current_weather.clouds
        humidity = current_weather.humidity
        temperature = current_weather.temperature('celsius')['temp']
        feelsLike = current_weather.temperature('celsius')['feels_like']
        windSpeed =  current_weather.wind()['speed']
        pressure = current_weather.barometric_pressure(unit='inHg')['press']
        details = current_weather.detailed_status
        # Get the time
        srise = datetime.datetime.fromtimestamp(current_weather.srise_time)
        sset = datetime.datetime.fromtimestamp(current_weather.sset_time)
        srise_string = srise.strftime('%Y-%m-%d %H:%M:%S')
        sset_string = sset.strftime('%Y-%m-%d %H:%M:%S')

        is_raining =current_weather.rain
        if is_raining:
            rain = True
        else:
            rain = False
        # Create a dictionary to hold the weather data
        
        return {
            "location": f'{self.city}, {self.Country}',
            "temperature": temperature,
            "feels_Like": feelsLike,
            "clouds": clouds,
            "wind_speed": windSpeed,
            "humidity": humidity,
            "pressure": pressure,
            "rain": rain,
            "details": details,
            "sun_rise": srise_string,
            "sun_set" : sset_string
        }
    
    
    def save_weather_to_json(self):
        weather_data = self.get_weather_data()
        # Create the file name to label where it comes from
        jsonFileName = f'data\{self.city}-{self.Country}_weather-data.json'
        # Write the json file
        with open (jsonFileName, "w") as json_file:
            json.dump(weather_data, json_file, indent=4)
        #  print the content and file on completion (debugging)
        print(f'{weather_data}\n Written to {jsonFileName}')
