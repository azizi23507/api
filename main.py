import requests
import json
response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=48.36&longitude=13.0&current_weather=true")
print(json.dumps(response.json(), indent=4))

print(response.json()["current_weather"]["temperature"])

print(response.status_code)
print(response.headers)