from flask import Flask, request, jsonify
import csv
app = Flask(__name__)

@app.route("/")
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

# http://127.0.0.1:5000/sightings?country=US&page=3&per_page=5
@app.route("/sightings", methods=["GET"])
def get_sightings():
    country = request.args.get('country', '')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    ufo_sightings = load_ufo_data('scrubbed.csv')
    filter_sightings = []

    if not country:
        return jsonify(ufo_sightings)

    for sighting in ufo_sightings:
        if country.upper() == sighting['country'].upper():
            filter_sightings.append(sighting)

    start = (page - 1) * per_page
    end = start + per_page
    
    return jsonify(filter_sightings[start:end])

def load_ufo_data(filepath):
    sightings = []
    with open(filepath, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            sightings.append(row)

    return sightings

@app.route('/top_ten', methods=['GET'])  
def top_ten():
    sightings = load_ufo_data('scrubbed.csv')[:10]
    html_string = ""
    for sighting in sightings:
        html_string += f"<p>Location: {sighting["city"]}, {sighting["state"]}, {sighting["country"]}. Date: {sighting["date posted"]}</p>"

    return f"""
    <html>
        <head>
            <title>Top Ten UFO Sightings</title>
        </head>
        <body>
            <h1>Top Ten Sightings</h1>
            {html_string}
        </body>
    </html>
    """

@app.route('/research_stations', methods=['GET'])
def get_research_stations():
    stations = []
    with open('research_stations.csv', mode='r') as file:
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
        return jsonify({'error':'Name and location are required'}), 400
    
    with open('research_stations.csv', mode='a', newline='') as file:
        fieldnames = ['name','location']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({'name': name, 'location': location})
    
    return jsonify({'message': 'Research station added!'}), 201