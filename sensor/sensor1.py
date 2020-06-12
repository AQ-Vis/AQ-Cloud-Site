import requests
import json

url = 'http://localhost:5000/add_sensor_data'
text = {
    "device_id": "test002",
    "timestamp": "13:47:27:28",
    "altitude": 400.56,
    "latitude": -31.234,
    "longitude": 91.432,
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

x = requests.post(url, json = text)

print(x.text)
