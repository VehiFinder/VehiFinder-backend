from flask import Flask, request, jsonify
import webscraping as ws
from webscraping import scrape_function

app=Flask(__name__)

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
    return jsonify([car.__dict__ for car in carName])

if __name__ == "__main__":
    app.run(debug=True)