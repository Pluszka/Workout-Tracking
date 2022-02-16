import os
import requests
import datetime as dt

ID = os.environ.get('nutritionix_ID')
KEY = os.environ.get('nutritionix_key')

GENDER = "female"
WEIGHT_KG = 61.5
HEIGHT_CM = 164
AGE = 19

SHEETY_ENDPOINT = os.environ.get('SHEETY_WORKOUTS')
NUTRI_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'

nutri_params_exercise = {
 "query": input('Which exercises have you done?(+amount of time/reps)').lower(),
 "gender": GENDER,
 "weight_kg": WEIGHT_KG,
 "height_cm": HEIGHT_CM,
 "age": AGE
}

header = {
    'x-app-id': ID,
    'x-app-key': KEY
}

response = requests.post(url=NUTRI_ENDPOINT, json=nutri_params_exercise, headers=header)
response.raise_for_status()
data = response.json()

for exercise in data['exercises']:
    params_row = {
        'workout': {
            'date': dt.date.today().strftime("%d/%m/%Y"),
            'time': dt.datetime.now().time().strftime("%X"),
            'exercise': exercise['user_input'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories'],
        }
    }
    response = requests.post(url=SHEETY_ENDPOINT, json=params_row)
    print(response.text)
