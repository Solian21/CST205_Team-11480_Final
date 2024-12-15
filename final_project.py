# Title; Final Project - CST205
# Author: Carlos Solian, Aryll Pacheco, Bryson Ruck, & Sarah Wafa


# Adding Them to Git
# git add .
# Commit
# git commit -m "Something Meaningful"
# Push
# git push -u origin main

from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
import requests



app = Flask(__name__)
boostrp = Bootstrap5(app)
# API
base_url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": 36.6111,
	"longitude": -121.8516,
	"current": "temperature_2m",
	"hourly": "temperature_2m",
	"temperature_unit": "fahrenheit",
	"wind_speed_unit": "mph",
	"precipitation_unit": "inch",
	"timezone": "America/Los_Angeles"
}
# precipitation_unit=inch&timezone=America%2FLos_Angeles
url = f'https://api.open-meteo.com/v1/forecast?latitude={params["latitude"]}&longitude={params["longitude"]}&current={params["current"]}&hourly={params["hourly"]}&temperature_unit={params["temperature_unit"]}&wind_speed_unit={params["wind_speed_unit"]}&precipitation_unit={params["precipitation_unit"]}&timezone={params["timezone"]}'
print(url)
@app.route('/')
def homepage():
    weather = get_weather()
    # current_temp = weather['crrent_weather']['temperature']
    return render_template('homepage.html')

# Aryll's Home Page
@app.route('/Aryll')
def AryllPage():
    return render_template('aryllhomepage.html')

@app.route('/AryllPottery')
def pottery():
    return render_template('aryllpottery.html')

@app.route("/AryllReading")
def books():
    return render_template('aryllbooks.html')

# Carlos's Home Page
@app.route('/Carlos')
def Carlos():
    return render_template('CarlosHomePage.html')

# Carlos's Major Page
@app.route('/Carlos/Major')
def CarlosMajor():
    return render_template('carlosMajor.html')

# Carlos's Music Page
@app.route('/Carlos/Music')
def CarlosMusic():
    return render_template('carlosMusic.html')

# Carlos's Hobbies Page
@app.route('/Carlos/Hobbies')
def CarlosHobbies():
    return render_template('carlosHobbies.html')

@app.route('/Bryson')
def Bryson():
    return render_template('Bryson.html')
@app.route('/Bryson/Guitar')
def Guitar():
    return render_template('gutiar.html')

@app.route('/Bryson/Music')
def Music():
    return render_template('Music.html')

@app.route('/Bryson/Walking')
def Walking():
    return render_template('walking.html')
@app.route('/Bryson/Electronics')
def Electronics():
    return render_template('Electronics.html')

#Sarah's Home Page
@app.route('/sarah')
def Sarah():
    return render_template('sarahhomepage.html')

@app.route('/SarahHorror')
def horror():
    return render_template('sHorror.html')

@app.route('/SarahSM')
def spdrmn():
    return render_template('sarahspiderman.html')

