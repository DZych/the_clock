import requests



def get_current_weather():
    location_code = "2-3099180"

    # https://www.yr.no/api/v0/locations/2-3099180/forecast/currenthour
    current_weather_url = f"https://www.yr.no/api/v0/locations/{location_code}/forecast/currenthour"

    response = requests.get(current_weather_url)

    if response.status_code == 200:
        return response.json() # response.json()['temperature']['value']
    else:
        return "No internet connection"
