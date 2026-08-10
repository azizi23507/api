import requests
import json
response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=48.36&longitude=13.0&current_weather=true")
print(json.dumps(response.json(), indent=4))
print(response.json()["current_weather"]["temperature"])
print(response.status_code)
print(response.headers)


response = requests.get("https://api.github.com/users/azizi23507")
print(response.status_code)
print(response.json()["name"])
print(response.json()["public_repos"])
print(json.dumps(response.json(), indent=4))



response = requests.get(
    "https://api.github.com/search/users",
    params={"q": "location:USA", "per_page": 3})
print(json.dumps(response.json(), indent=4))
