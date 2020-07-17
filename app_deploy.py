#--------------------------------------------------#
#THIS IS THE VERSION FOR THE CLOUD USING INTERNAL IP
#gunicorn app_deploy:app --bind 0.0.0.0:8000
#--------------------------------------------------#

from bson.json_util import dumps
import json
from flask import Flask, request, render_template, session, redirect, url_for, flash, Response, abort, render_template_string, send_from_directory
#from flask_cors import CORS
import requests
from datetime import date
from bson.objectid import ObjectId
from elasticsearch import Elasticsearch

app = Flask(__name__)
#CORS(app)
#app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

es = Elasticsearch([{'host': '10.128.0.6', 'port': 9200}])

@app.route('/add_new_device', methods=['POST'])
def add_new_device():
	#Maybe some authentication can be added to prevent unauthorized people from adding new devices
	inputData = request.json
	data = {'device_id':inputData['device_id']}
	currdata = es.search(index='device_info', id=inputData['device_id'])

	es.index(index='device_info', id=inputData['device_id'], body=data)
	return Response(status=200)

@app.route('/add_sensor_data', methods=['POST'])
def add_sensor_data():
	inputData = request.json
	device_id = inputData['device_id']
	today = date.today()
	currdate = today.strftime("%d-%m-%Y")
	currdate = today.strftime("%Y-%m-%d")
	lastcontact = currdate + str("\'T\'") + str(inputData['timestamp'])
	data = {'device_id':inputData['device_id'], 'timestamp':lastcontact, 'altitude':inputData['altitude'], 'location':{'lat':inputData['latitude'], 'lon':inputData['longitude']}, 'aq1':{'pm10':inputData['aq1']['pm10'], 'pm75':inputData['aq1']['pm75'], 'pm25':inputData['aq1']['pm25']}, 'aq2':{'pm10':inputData['aq2']['pm10'], 'pm75':inputData['aq2']['pm75'], 'pm25':inputData['aq2']['pm25']}, 'aq3':{'pm10':inputData['aq3']['pm10'], 'pm75':inputData['aq3']['pm75'], 'pm25':inputData['aq3']['pm25']}, 'battery_level':inputData['battery_level']}
	mn = es.index(index=device_id, body=data)
	#print(mn)
	#print(lastcontact)
	return Response(status=200)

@app.route('/get_data', methods=['GET'])
def get_data():
	data = es.search()
	return data

#Another Basic Route
@app.route('/')
def homepage():
	val=es.index(index='my_index', id=1, body={'text': 'this is a test'})
	return val
	#return render_template('index.html')
