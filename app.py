import json
from flask import Flask 
import Weather


app = Flask(__name__)


@app.route("/")
def hello():
	return "Hello, World\t\t\t" * 6


@app.route("/Weather-Cluj")
def weather():
	temperature = json.dumps(Weather.Weather())
	return f"{temperature}"

@app.route("/Weather/my-cities/")
def weather_multiple_cities():
	return "Cluj : 15, New York : 10"

