#logic for flight details

import json

with open("all_flights.json", "r") as f:
    json_data = f.read()

flight_data = json.loads(json_data)

for flights in flight_data:
    if flights['origin'] == From and flights['destination'] == to:
        flight = flights
        print(flight)