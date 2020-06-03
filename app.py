import pymongo
from bson.json_util import dumps
import json
from flask import Flask, request, render_template, session, redirect, url_for, flash, Response, abort, render_template_string, send_from_directory
from flask_cors import CORS
import requests
from datetime import date
from bson.objectid import ObjectId

app = Flask(__name__)
CORS(app)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = b'\xd2(*K\xa0\xa8\x13]g\x1e9\x88\x10\xb0\xe0\xcc'

#Loads the Database and Collections
mongo = pymongo.MongoClient('mongodb+srv://admin:temporarypassword@cluster0-4qcuj.mongodb.net/test?retryWrites=true&w=majority', maxPoolSize=50, connect=True)
db = pymongo.database.Database(mongo, 'aq_db_1')

@app.route('/test/test')
def test():
	return "Works"

#Another Basic Route
@app.route('/')
def homepage():
	return render_template('index.html')

#Basic JSON input
@app.route('/api/input_data', methods=['POST'])
def input_data():
	inputData = dict(request.json)
	device_id = str(inputData['device_id'])
	ppm = int(inputData['ppm'])
	print(ppm,device_id)
	return Response(status=200)

@app.route('/api/get_device_list')
def get_device_list():
	Device_Info = pymongo.collection.Collection(db, 'Device_Info')
	devices = json.loads(dumps(Device_Info.find()))
    data = {'count':len(devices), data:devices}
	return data

@app.route('/api/add_sensor_data', methods=['POST'])
def add_sensor_data():
	inputData = request.json
	Device_Info = pymongo.collection.Collection(db, 'Device_Info')
	devices = json.loads(dumps(Device_Info.find({'device_id':inputData['device_id']})))
	today = date.today()
	currdate = today.strftime("%d-%m-%Y")
	lastcontact = currdate + str(' ') + str(inputData['timestamp'])
	if(len(devices) == 0):
		Device_Info.insert_one({'device_id':inputData['device_id'], 'last_contact':lastcontact, 'last_altitude':inputData['altitude'], 'last_latitude':inputData['longitude'], 'last_longitude':inputData['longitude']})
	else:
		Device_Info.update_one({'$set':}{'device_id':inputData['device_id'], 'last_contact':lastcontact, 'last_altitude':inputData['altitude'], 'last_latitude':inputData['longitude'], 'last_longitude':inputData['longitude']})
	data = {'count':len(devices), data:devices}
	Sensor_Info.insert_one({'device_id':inputData['device_id'], 'timestamp':lastcontact, 'altitude':inputData['altitude'], 'latitude':inputData['longitude'], 'longitude':inputData['longitude'], 'aq1_pm10':inputData['aq1_pm10'], 'aq1_pm75':inputData['aq1_pm75'], 'aq1_pm25':inputData['aq1_pm25'], 'aq2_pm10':inputData['aq2_pm10'], 'aq2_pm75':inputData['aq2_pm75'], 'aq2_pm25':inputData['aq2_pm25'], 'aq3_pm10':inputData['aq3_pm10'], 'aq3_pm75':inputData['aq3_pm75'], 'aq3_pm25':inputData['aq3_pm25'])
	return data

@app.route('/api/get_data')
def get_data():
	data = {'count':5,'data':[{'device_id':1,'datetime':'2020-05-30 13:45:05','ppm':450},{'device_id':1,'datetime':'2020-05-30 13:46:15','ppm':455},{'device_id':1,'datetime':'2020-05-30 13:47:18','ppm':451},{'device_id':1,'datetime':'2020-05-30 13:48:01','ppm':443},{'device_id':1,'datetime':'2020-05-30 13:49:23','ppm':453}]}
	return data

@app.route('/api/get_locations')
def get_locations():
	data = {'count':3,'data':[{'device_id':1,'lat':30.05,'long':-70.05},{'device_id':2,'lat':30.15,'long':-7.15},{'device_id':3,'lat':30.25,'long':-70.25}]}
	return data

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r
