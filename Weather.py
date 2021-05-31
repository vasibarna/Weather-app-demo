import requests

cities = ["Cluj-Napoca", "Timisoara", "Iasi", "Paris", "Berlin", "Madrid", "Barcelona", "Viena"]

def Weather(city):
	if city in cities: 
		url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID=e943095734d9837eb56de847ff140147"
		response = requests.get(url)
		weather  = response.json()
		temp = weather["main"]["temp"] - 273.15
		return {f"{city}" : "%.2f" % (temp)}
