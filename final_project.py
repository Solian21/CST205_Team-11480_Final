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


app = Flask(__name__)
boostrp = Bootstrap5(app)




@app.route('/')
def homepage():
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

@app.route('/Bryson')
def Bryson():
    return render_template('Bryson.html')


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

