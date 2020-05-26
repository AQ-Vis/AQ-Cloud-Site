from flask import Flask, render_template, request, Response

app = Flask(__name__)

#Basic Route
@app.route('/')
def root():
	return "Welcome!"

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
