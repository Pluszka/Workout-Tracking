import os
import requests

ID = os.environ.get('nutritionix_id')
KEY = os.environ.get('nutritionix_key')

NUTRI_ENDPOINT = 'https://trackapi.nutritionix.com/v2/search/instant'

nutri_params = {

}

response = requests.get(url=NUTRI_ENDPOINT)