#import pymongo
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

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

@app.route('/api/add_new_device', methods=['POST'])
def add_new_device():
	#Maybe some authentication can be added to prevent unauthorized people from adding new devices
	inputData = request.json
	data = {'device_id':inputData['device_id']}
	currdata = es.search(index='device_info', id=inputData['device_id'])

	es.index(index='device_info', id=inputData['device_id'], body=data)
	return Response(status=200)

#Another Basic Route
@app.route('/')
def homepage():
	es.index(index='my_index', id=1, body={'text': 'this is a test'})
	return Response(status=200)
	#return render_template('index.html')
