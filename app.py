import json
from flask import Flask 
import Weather as W

app = Flask(__name__)

@app.route("/<city>")
def weather(city):
	temperature = json.dumps(W.Weather(city))
	return f"{temperature}"
