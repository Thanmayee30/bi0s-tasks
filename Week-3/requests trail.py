import requests
import json
country = input("Enter country code: ")
pincode = int(input("Enter pincode: "))
url = ("https://api.zippopotam.us/%s/%s" % (country , pincode))
response = requests.get(url)
json_response= response.json()
country_rep = json_response['country']
place_repository = json_response['places'][0]
print(f'Country: {country_rep}')
print(f'Place Name: {place_repository["place name"]}')
print(f'state: {place_repository["state"]}')


