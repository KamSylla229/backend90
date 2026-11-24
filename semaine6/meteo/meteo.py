import truststore
truststore.inject_into_ssl()
import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {"latitude": 6.37, "longitude": 2.42, "current": "temperature_2m,relative_humidity_2m,wind_speed_10m", "timezone": "Africa/Lagos"}

reponse = requests.get(url, params=params, timeout=10)

if reponse.status_code != 200:
    print(f"Erreur : code {reponse.status_code}")
else :
    donnees = reponse.json()
    actuel = donnees["current"]
    print(f"Cotonou — {actuel['time']} : {actuel['temperature_2m']} °C, humidité {actuel['relative_humidity_2m']} %, vent {actuel['wind_speed_10m']} km/h ")
    