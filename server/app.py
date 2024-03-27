from flask import Flask #flask run
from flask import request, jsonify

app = Flask(__name__)

# Testing API endpoint
@app.get("/api/test-api")
def test_api():
    return jsonify({"message": "API Working"})