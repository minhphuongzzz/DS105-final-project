import requests
import numpy as np
import pandas as pd
from collections import defaultdict
import json
from tqdm import tqdm

weather = defaultdict(list)

df = pd.read_csv('dataset/processed-glc.csv')

i0 = np.arange(0, 3971)
i1 = np.arange(3971,7502)
i2 = np.arange(7502,11034)

api_key = 'QG5S75PHN22F64Z46VPZLZRLA' 

for i in i1: # i0, i1 or i2
  print(i)

  lat = df['latitude'][i]
  long_ = df['longitude'][i]
  date = df['event_date'][i][:10]
  
  url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{},{}/{}?unitGroup=metric&key={}&include=obs".format(lat,long_,date,api_key)
  response = requests.get(url)
  res = response.json()
  weather_data = res['days'][0]

  for key, val in weather_data.items():
      weather[key].append(val)
  if 'source' in weather:
    weather.pop('source')

  weather_df = pd.DataFrame(weather)
  # print(df['event_id'][i1[0]:i1[-1]+1])
  weather_df.insert(loc=0, column='event_id', value = df['event_id'][i1[0]:i1[-1]+1])
  weather_df.to_csv('weather_{}-{}.csv'.format(i1[0], i1[-1]+1),index=False)