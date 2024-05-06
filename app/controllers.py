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

@app.route('/api/autos')
def autos():
    page_number = int(request.args.get('page'))
    carName = scrape_function("tucarro", "", page_number)
    models.CarModel.save_car(carName)
    threading.Timer(7.0, delete_cars, args=[carName]).start()
    return json_util.dumps([car.__dict__ for car in carName])

# @app.route('/autos/<string:car_name>/<string:year>')
# def get_autos_by_year(car_name, year):
#     carName = scrape_function("tucarro", car_name)
#     for car in carName:
#         models.CarModel.save_car(car)
#     cars = models.CarModel.get_cars_by_year(year)
#     threading.Timer(30.0, delete_cars, args=[carName]).start()
#     return json_util.dumps([car for car in cars])

@app.route('/api/autos/<string:car_name>')
def get_autos_by_filters(car_name):
    filters={}
    page_number = int(request.args.get('page'))
    carName = scrape_function("tucarro", car_name, page_number)
    # for car in carName:
    models.CarModel.save_car(carName)
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
    
    # Parámetros para la paginación
    # page = int(request.args.get('page', 1))
    # autos_por_pagina = int(request.args.get('autos_por_pagina', 48))
    
    cars = models.CarModel.get_cars_by_filters(filters)
    
     # Se calcula el índice de inicio y fin
    # inicio = (page - 1) * autos_por_pagina
    # fin = inicio + autos_por_pagina
    # cars = cars[inicio:fin]
    
    return json_util.dumps([car for car in cars])


