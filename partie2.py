import pandas as pd
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

api_neo = 'https://api.nasa.gov/neo/rest/v1/feed'

params = {
    'api_key' : API_KEY ,
    'date_start' : '2024-06-23',
    'date_end' : '2024-06-25'
}

response = requests.get(api_neo, params)

todos = response.json()

# Extraire les données sur les astéroïdes pour la date spécifique
neo_data = todos['near_earth_objects']['2024-06-25']

asteroid_ids = []
asteroid_names = []
min_diameters_km = []
absolute_magnitudes = []
relative_velocities = []

for i in neo_data:
    asteroid_ids.append(i['id'])
    asteroid_names.append(i['name'])
    min_diameters_km.append(i['estimated_diameter']['kilometers']['estimated_diameter_min'])
    absolute_magnitudes.append(i['absolute_magnitude_h'])
    relative_velocities.append(i['close_approach_data'][0]['relative_velocity']['kilometers_per_second'])

df = pd.DataFrame({
    'ID Astéroïde': asteroid_ids,
    'Nom Astéroïde': asteroid_names,
    'Diamètre Minimal Estimé (km)': min_diameters_km,
    'Magnitude Absolue': absolute_magnitudes,
    'Vitesse Relative (km/s)': relative_velocities
})
print(df)

df.to_csv('data.csv')

print(todos.status_code)

