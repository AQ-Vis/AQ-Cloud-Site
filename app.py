#--------------------------------------------------#
#THIS IS THE VERSION FOR THE Local testing using external static IP
#flask run
#--------------------------------------------------#

import json
from flask import Flask, request, Response
import requests
from datetime import date
from elasticsearch import Elasticsearch
import os

if 'ELASTICSEARCH_URL' in os.environ:
	es_url = os.environ['ELASTICSEARCH_URL']
else:
	print("Please provide Elasticsearch URL as Environment Variable")
	exit()

app = Flask(__name__)
#CORS(app)
#app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

#es_url = "104.196.0.115"

es = Elasticsearch([{'host': es_url, 'port': 9200}])

@app.route('/device/<device_id>', methods=['GET'])
def add_new_device(device_id):
	#Maybe some authentication can be added to prevent unauthorized people from adding new devices
	data = {
	    "mappings": {
	        "properties": {
	            "timestamp": {
	                "type": "date"
	            },
	            "location": {
	                "type": "geo_point"
	            }
	        }
	    }
	}
	x = requests.put(es_url+":9200/"+device_id, json = data)
	return (x.text,str(x.status_code))



@app.route('/sensor/data', methods=['POST'])
def add_sensor_data():
	inputData = request.json
	device_id = inputData['device_id']
	today = date.today()
	currdate = today.strftime("%Y-%m-%d")
	lastcontact = currdate + str("T") + str(inputData['timestamp'])
	data = {'device_id':inputData['device_id'], 'timestamp':lastcontact, 'altitude':inputData['altitude'], 'location':{'lat':inputData['latitude'], 'lon':inputData['longitude']}, 'aq1':{'pm10':inputData['aq1']['pm10'], 'pm75':inputData['aq1']['pm75'], 'pm25':inputData['aq1']['pm25']}, 'aq2':{'pm10':inputData['aq2']['pm10'], 'pm75':inputData['aq2']['pm75'], 'pm25':inputData['aq2']['pm25']}, 'aq3':{'pm10':inputData['aq3']['pm10'], 'pm75':inputData['aq3']['pm75'], 'pm25':inputData['aq3']['pm25']}, 'battery_level':inputData['battery_level']}
	mn = es.index(index=device_id, body=data)
	return Response(status=200)

@app.route('/data', methods=['GET'])
def get_data():
	data = es.search()
	return data

#Testing routes
@app.route('/')
def homepage():
	val=es.index(index='my_index', id=1, body={'text': 'this is a test'})
	return val

@app.route('/test')
def test():
	return("Works")
