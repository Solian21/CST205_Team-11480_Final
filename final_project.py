# Title; Final Project - CST205
# Author: Carlos Solian, Aryll Pacheco, Bryson Ruck, & Sarah Wafa

from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
boostrp = Bootstrap5(app)

@app.route('/')
def homepage():
    return render_template('homepage.html')