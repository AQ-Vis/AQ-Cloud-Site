from flask import Flask, render_template, request, Response

app = Flask(__name__)

#Basic Route
@app.route('/')
def root():
	return "Welcome to AQ Cloud Site Visualization"

@app.route('/test/test')
def test():
	return "Works"

#Another Basic Route
@app.route('/homepage')
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

@app.route('/api/get_data')
def get_data():
	data = {'count':5,'data':[{'device_id':1,'datetime':'2020-05-30-13-45-05','ppm':450},{'device_id':1,'datetime':'2020-05-30-13-46-15','ppm':455},{'device_id':1,'datetime':'2020-05-30-13-47-18','ppm':451},{'device_id':1,'datetime':'2020-05-30-13-48-01','ppm':443},{'device_id':1,'datetime':'2020-05-30-13-49-23','ppm':453}]}
	return data

@app.route('/api/get_locations')
def get_locations():
	data = {'count':3,'data':[{'device_id':1,'lat':30.05,'long':-70.05},{'device_id':2,'lat':30.15,'long':-7.15},{'device_id':3,'lat':30.25,'long':-70.25}]}
	return data
