from flask import Flask #flask run
from flask import request, jsonify

app = Flask(__name__)

# Testing API Endpoint
@app.get("/api/test-api")
def test_api():
    return jsonify({"message": "API Working"})

# Post NBA Player Name

# Get NBA Player Career Stats

# Get NBA Player Past 10 Game Log

# Get Prediction for Next 5 Games Through Model
