import requests

name = "john"
age_response = requests.get(url=f"https://api.agify.io?name={name}")
age = age_response.json()["age"]

print(age)