import os
import requests

ID = os.environ.get('nutritionix_ID')
KEY = os.environ.get('nutritionix_key')

NUTRI_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'

nutri_params_exercise = {
 "query": input('Which exercises have you done?(+amount of time/reps)'),
 "gender": "female",
 "weight_kg": 61.5,
 "height_cm": 164,
 "age": 19
}

header = {
    'x-app-id': ID,
    'x-app-key': KEY
}

response = requests.post(url=NUTRI_ENDPOINT, json=nutri_params_exercise, headers=header)
response.raise_for_status()
data = response.json()
print(data)
