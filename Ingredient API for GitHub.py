import requests
import random

ingredient = input("What ingredient would you like to use? ")

#sign up on edamam website to obtain App ID & App key
YOUR_APP_ID = ""
YOUR_APP_KEY = ""

url = "https://api.edamam.com/search?q={}&app_id={}&app_key={}".format(ingredient, YOUR_APP_ID, YOUR_APP_KEY)

response = requests.get(url)
response.raise_for_status()

data = response.json()
results = data['hits']

random_result = random.choice(results)

recipe = random_result["recipe"]

print(recipe["label"], recipe["url"])
