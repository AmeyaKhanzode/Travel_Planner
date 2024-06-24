from flask import Flask, render_template, redirect, request
from cities import List_of_cities  
import spots as s
import description as d
import  json
import hotels as h

to = None
From = None

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', cities=List_of_cities) 

@app.route('/start', methods=["GET"])
def start():
    global to
    global From
    From = request.args.get('From')
    to = request.args.get('To')
    days = request.args.get('days')
    return redirect('/location')

@app.route('/page')
def page():
    return render_template('location.html')


@app.route('/location')
def tour():
    
    locations = []
    for k, v in d.description[to].items():
        locations.append({'name': k, 'desc': v})
        
    return render_template('location.html', locations=locations, to=to, spots=s.spots[to])

@app.route("/pages")
def hotel():
    return redirect('/hotel')

@app.route("/hotel")
def hotels():
    hotels_list = h.hotels.get(to)
    if hotels_list:
        return render_template('hotel.html', hotels_list=hotels_list)
    return render_template('hotel.html')

@app.route("/about")
def about():
    return redirect("/flight")


import json

with open("all_flights.json", "r") as f:
    json_data = f.read()

flight_data = json.loads(json_data)

@app.route("/flight")
def flight():
    for flight in flight_data:
        if flight["origin"] == From and flight["destination"] == to:
            flight_origin = flight["origin"]
            flight_destination = flight["destination"]
            flight_price = flight["price"]
            flight_carrier = flight["carrier"]
            return render_template('flight.html', flight_data=flight, flight_origin=flight_origin, flight_destination=flight_destination, flight_price=flight_price, flight_carrier=flight_carrier)
