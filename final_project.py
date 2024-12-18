# Course: CST205
# Title: Final Project - CST205
# Abstract: This project is our final for the CST205 class at CSUMB. Our group decided to make a presentaiton about us and who we are as a friend group as well as to try and inform our peers about the CS++ at CSUMB.
# Author: Carlos Solian, Aryll Pacheco, Bryson Ruck, & Sarah Wafa
#Github Link: https://github.com/Solian21/CST205_Team-11480_Final


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
# This API is able to give the current weather given the latitude and longitude. It runs on 15 minutes intervals.
base_url = "https://api.open-meteo.com/v1/forecast"
params = {
    # Latitude and Longitude are set for seaside
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
weather = requests.get(url).json()

@app.route('/')
def homepage():
    current_temp = weather['current']['temperature_2m']
    temp_unit = weather['current_units']['temperature_2m']
    return render_template('homepage.html', current_temp=current_temp, temp_unit=temp_unit)

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
    return render_template('guitar.html')

@app.route('/Bryson/Music')
def Music():
    return render_template('Music.html')

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

@app.route('/SarahSMCup')
def cup():
    return render_template('cup.html')

@app.route('/SarahSMPlush')
def plushies():
    return render_template('smplushies.html')

@app.route('/SarahSMLego')
def legos():
    return render_template('smlego.html')