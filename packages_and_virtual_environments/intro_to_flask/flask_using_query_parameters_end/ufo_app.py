import csv
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>UFO Sightings</title>
        </head>
        <body>
            <h1>Welcome to the UFO Sightings API</h1>
            <p>Use the /sightings route to get UFO sighting data.</p>
        </body>
    </html>
    """

def load_ufo_data(filepath):
    sightings = []
    with open(filepath, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            sightings.append(row)
    return sightings

@app.route('/ufo_sightings', methods=['GET'])
def get_sightings():
    country = request.args.get('country', '')
    scrubbed_sightings = load_ufo_data('data/scrubbed.csv')
    filtered_sightings = scrubbed_sightings.copy()
    for sighting in scrubbed_sightings:
        if country and sighting['country'].lower() != country.lower():
            filtered_sightings.remove(sighting)
    return jsonify(filtered_sightings)

@app.route('/research_stations', methods=['GET'])
def get_research_stations():
    stations = []
    with open('data/research_stations.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            stations.append(row)
    return jsonify(stations)


@app.route('/add_research_station', methods=['POST'])
def add_research_station():

    data = request.get_json()
    name = data.get('name')
    location = data.get('location')
    if not name or not location:

        return jsonify({'error': 'Name and location are required'}), 400
    with open('data/research_stations.csv', mode='a', newline='') as file:
        fieldnames = ['name', 'location']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({'name': name, 'location': location})
    return jsonify({'message': 'Research station added successfully'}), 201