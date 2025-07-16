import requests

gender = requests.get("https://api.genderize.io?name=peter")
gender = gender.json()["name"]

age = requests.get("https://api.agify.io?name=michael")
age = age.json()["name"]

print(gender)
print()
print(age)