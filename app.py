import json
from flask import Flask 
import Weather as W

app = Flask(__name__)


@app.route(f"/{W.city}")
def weather():
	temperature = json.dumps(W.Weather(W.city))
	return f"{temperature}"

