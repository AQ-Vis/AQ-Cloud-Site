import random
from locust import HttpUser, task, between
from datetime import datetime

class QuickStartUser(HttpUser):
    wait_time = between(5, 10)

    @task
    def load_page(self):
        #self.client.get("/")
        now = datetime.now()
        currtime = now.strftime("%Y-%m-%dT%H:%M:%S.%f")
        data = {
            "device_id": "loadtest002",
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
        data['timestamp'] = currtime
        self.client.post("/add_sensor_data", json=data)
