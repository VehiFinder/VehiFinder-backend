from flask import Flask, request, jsonify
import webscraping as ws

app=Flask(__name__)

@app.route('/')
def root():
    return "¡Hola mundo!"

@app.route('/autos')
def autos():
    tucarro = ws.tucarro
    autocosmos = ws.autocosmos
    cars = tucarro + autocosmos
    return jsonify([car.__dict__ for car in cars])

if __name__ == "__main__":
    app.run(debug=True)