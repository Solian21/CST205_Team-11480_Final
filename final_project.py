# Title; Final Project - CST205
# Author: Carlos Solian, Aryll Pacheco, Bryson Ruck, & Sarah Wafa

from flask import Flask, render_templates
from flask_bootstrp import Bootstrap5

app = Flask(__name__)
boostrp = Bootstrap5(app)

@app.route('/')
def homepage():
    return render_templates('homepage.html')