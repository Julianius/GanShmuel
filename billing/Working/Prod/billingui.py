from flask import Flask, render_template, request, jsonify
from flask import Response
import json
import requests
import random
import os
import calendar
from datetime import datetime
from werkzeug.wrappers import response
import subprocess
import sys

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
    # Add Navigiation bar to our APIs


@app.route('/bills')
def bills():
    return render_template('bills.html')
    # Add Navigiation bar to our APIs

@app.route('/bills/<provider_id>')
def bills_spes(provider_id):
    return render_template('bills_spec.html')
    # Add Navigiation bar to our APIs

@app.route('/health')
def health():
    return render_template('health.html')

@app.route('/providers')
def provider():
    return render_template('providers.html')


@app.route('/rates')
def rates():
    return render_template('rates.html')


@app.route('/trucks')
def truck():
    return render_template('trucks.html')


@app.route('/trucks/<truck_number>')
def truck_id(truck_number):
    return render_template('truck_id.html')






if __name__ == '__main__':


    app.run(debug=True, port=8081, host='0.0.0.0')
