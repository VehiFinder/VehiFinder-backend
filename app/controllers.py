from bson import json_util
from flask import Flask, request, jsonify
from app import app
from app import models
import threading
from utils.webscraping import scrape_function

@app.route('/')
def root():
    return "¡Hola mundo!"

# @app.route('/autos')
# def autos():
#     cars = ws.tucarro
#     return jsonify([car.__dict__ for car in cars])

@app.route('/autos/<string:car_name>')
def autos(car_name):
    carName = scrape_function("tucarro", car_name)
    for car in carName:
        models.CarModel.save_car(car)
    return json_util.dumps([car.__dict__ for car in carName])