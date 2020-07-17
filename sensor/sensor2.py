import requests
import json
from datetime import datetime
from time import sleep
import random

url = 'http://localhost:5000/add_sensor_data'
#url = 'http://34.70.119.223:8000/add_sensor_data'

data = {
    "device_id": "gcptest007",
    "timestamp": "",
    "altitude": 400.56,
    "latitude": 11.976750,
    "longitude": 78.575279,
    "battery_level": 75.1,
    "aq1": {
        "pm10": 51.1,
        "pm75": 71.3,
        "pm25": 121.3
    },
    "aq2": {
        "pm10": 41.4,
        "pm75": 81.3,
        "pm25": 201.7
    },
    "aq3": {
        "pm10": 51.6,
        "pm75": 61.6,
        "pm25": 291.9
    }
}

while True:
    now = datetime.now()
    currtime = now.strftime("%H:%M:%S.%f")
    data['latitude']+=0.001
    data['longitude']+=0.001
    data['timestamp'] = currtime
    data['aq1']['pm10'] = random.uniform(40,80)
    data['aq1']['pm75'] = random.uniform(110,180)
    data['aq1']['pm25'] = random.uniform(10,14)
    data['aq2']['pm10'] = random.uniform(150,265)
    data['aq2']['pm75'] = random.uniform(10,80)
    data['aq2']['pm25'] = random.uniform(210,214)
    data['aq3']['pm10'] = random.uniform(0,1)
    data['aq3']['pm75'] = random.uniform(45,1050)
    data['aq3']['pm25'] = random.uniform(238,540)
    x = requests.post(url, json = data)
    print(x.status_code)
    #break
    sleep(1)
