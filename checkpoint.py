import requests

import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

#API_KEY = dotenv_values(".env")

API_KEY = os.getenv("API_KEY")

#API_KEY= {dotenv_values ​​(".env.shared" )}

api_url = "https://api.nasa.gov/planetary/apod"


params = {
    'api_key' : API_KEY ,
    'date' : '2024-06-25',
}

response = requests.get(api_url,params=params)

nasa = response.content('url')

print(nasa)
