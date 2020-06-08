import requests

url = 'http://localhost:5000/api/add_sensor_data'
myobj = {'somekey': 'somevalue'}

x = requests.post(url, data = myobj)

print(x.text)
