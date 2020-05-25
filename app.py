from flask import Flask, render_template

app = Flask(__name__)

#Basic Route
@app.route('/')
def root():
	return "Welcome!"
