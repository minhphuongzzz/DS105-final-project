Triet's Notes

```python
import requests
import numpy as np
from collections import defaultdict

weather = defaultdict(list)

i1 = np.arange(3971,7502)
i2 = np.arange(7503,11034)
api_key = 'Visual Crossing Weather API Key'

for i in i1: # i1 or i2
  lat = df['latitude'][i]
  long_ = df['longitude'][i]
  date = df['event_date'][i][:10]
  
  response = requests.get("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{},{}/{}?unitGroup=metric&key={}&include=obs".format(lat,long_,date,api_key))
  res = response.json()
  weather_data = res['days'][0]

  for key, val in weather_data.items():
      weather[key].append(val)

  weather.pop('source')
  weather_df = pd.DataFrame(weather)
  
  weather_df.insert(loc=0, column='event_id', value = df['event_id'][i1[0]:i1[-1]+1)
  weather_df.to_csv('weather_{}-{}.csv'.format(i1[0], i1[-1]+1),index=False)
```

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3971 entries, 0 to 3970
Data columns (total 35 columns):
 #   Column          Non-Null Count  Dtype  
---  ------          --------------  -----  
 0   event_id        3971 non-null   int64  
 1   datetime        3971 non-null   object 
 2   datetimeEpoch   3971 non-null   int64  
 3   tempmax         3961 non-null   float64
 4   tempmin         3961 non-null   float64
 5   temp            3503 non-null   float64
 6   feelslikemax    3961 non-null   float64
 7   feelslikemin    3961 non-null   float64
 8   feelslike       3503 non-null   float64
 9   dew             3491 non-null   float64
 10  humidity        3491 non-null   float64
 11  precip          3503 non-null   float64
 12  precipprob      0 non-null      object 
 13  precipcover     3961 non-null   float64
 14  preciptype      0 non-null      object 
 15  snow            378 non-null    float64
 16  snowdepth       434 non-null    float64
 17  windgust        1290 non-null   float64
 18  windspeed       3496 non-null   float64
 19  winddir         3302 non-null   float64
 20  pressure        2948 non-null   float64
 21  cloudcover      3503 non-null   float64
 22  visibility      3470 non-null   float64
 23  solarradiation  0 non-null      object 
 24  solarenergy     0 non-null      object 
 25  uvindex         3503 non-null   float64
 26  sunrise         3971 non-null   object 
 27  sunriseEpoch    3971 non-null   int64  
 28  sunset          3971 non-null   object 
 29  sunsetEpoch     3971 non-null   int64  
 30  moonphase       3971 non-null   float64
 31  conditions      3971 non-null   object 
 32  description     3971 non-null   object 
 33  icon            3971 non-null   object 
 34  stations        3513 non-null   object 
dtypes: float64(20), int64(4), object(11)
memory usage: 1.1+ MB
```
