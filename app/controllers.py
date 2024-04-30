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

def delete_cars(car_name):
    for car in car_name:
        models.CarModel.delete_car(car.nombre)

# @app.route('/autos/<string:car_name>')
# def autos(car_name):
#     carName = scrape_function("tucarro", car_name)
#     for car in carName:
#         models.CarModel.save_car(car)
#     threading.Timer(30.0, delete_cars, args=[carName]).start()
#     return json_util.dumps([car.__dict__ for car in carName])

# @app.route('/autos/<string:car_name>/<string:year>')
# def get_autos_by_year(car_name, year):
#     carName = scrape_function("tucarro", car_name)
#     for car in carName:
#         models.CarModel.save_car(car)
#     cars = models.CarModel.get_cars_by_year(year)
#     threading.Timer(30.0, delete_cars, args=[carName]).start()
#     return json_util.dumps([car for car in cars])

@app.route('/autos/<string:car_name>')
def get_autos_by_filters(car_name):
    filters={}
    
    carName = scrape_function("tucarro", car_name)
    for car in carName:
        models.CarModel.save_car(car)
    threading.Timer(7.0, delete_cars, args=[carName]).start()
    
    year_min = request.args.get('year_min')
    year_max = request.args.get('year_max')
    if year_min and year_max:
        filters["año"] = {"$gte": year_min, "$lte": year_max}
        
    year = request.args.get('year')
    if year:
        filters["año"] = year
    
    km = request.args.get('km')
    if km:
        filters["kilometraje"] = km
        
    km_min = request.args.get('km_min')
    km_max = request.args.get('km_max')
    if km_min and km_max:
        filters["kilometraje"] = {"$gte": km_min, "$lte": km_max}
        
    precio_min = request.args.get('precio_min')
    precio_max = request.args.get('precio_max')
    if precio_min and precio_max:
        filters["precio"] = {"$gte": precio_min, "$lte": precio_max}
    
    cars = models.CarModel.get_cars_by_filters(filters)
    return json_util.dumps([car for car in cars])


