# server.py
from flask import Flask, jsonify, request
from flask_cors import CORS
from data import get_all_events, add_event

app = Flask(__name__)
CORS(app)

# Home route
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Events API"})


# GET all events
@app.route("/events", methods=["GET"])
def get_events():
    return jsonify(get_all_events())


# POST new event
@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json()

    # Validation: title must be provided
    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    new_event = add_event(data["title"])
    return jsonify(new_event), 201


if __name__ == "__main__":
    app.run(debug=True)