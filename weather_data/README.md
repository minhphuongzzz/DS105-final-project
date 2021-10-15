Triet's Notes

```python
import requests

lat = df['latitude'][0]
long_ = df['longitude'][0]
date = df1['event_date'][0][:10]
api_Key = 'Visual Crossing Weather API Key'

response = requests.get("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{},{}/{}?unitGroup=metric&key={}&include=obs".format(lat,long_,date,api_key))
res = response.json()
weather_data = res['days'][0]
```
