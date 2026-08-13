import requests
import json
response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=48.36&longitude=13.0&current_weather=true")
print(response.json())
print(json.dumps(response.json(), indent=4))
print(response.json()["current_weather"]["temperature"])
print(response.status_code)
print("the header is ", response.headers)
print(response.request.headers)
print(response.headers.get("X-Ratelimit-Remaining"))

response = requests.get("https://api.github.com/users/azizi23507")
print(json.dumps(response.json(), indent=4))
print(response.status_code)
print(response.json()["name"])
print(response.json()["public_repos"])


response = requests.get(
    "https://api.github.com/search/users",
    params={"q": "location:USA", "per_page": 3})
print(json.dumps(response.json(), indent=4))

response = requests.get("https://api.github.com/users/torvalds")
raw_text = response.text          # the raw JSON string, unparsed
parsed = response.json()          # same thing, but parsed into a Python dict

print(type(raw_text))   # <class 'str'>
print(type(parsed))     # <class 'dict'>