from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory data store
events = [
    {"id": 1, "title": "Yoga in the Park"},
    {"id": 2, "title": "Lake 5K Run"}
]


@app.route("/", methods=["GET"])
def welcome():
    return jsonify({"message": "Welcome!"}), 200


@app.route("/events", methods=["GET"])
def get_events():
    return jsonify(events), 200


@app.route("/events", methods=["POST"])
def add_event():
    data = request.get_json()

    # Validate request data
    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    title = data["title"].strip()

    if title == "":
        return jsonify({"error": "Title cannot be empty"}), 400

    # Generate a new ID
    new_id = max((event["id"] for event in events), default=0) + 1

    new_event = {
        "id": new_id,
        "title": title
    }

    events.append(new_event)

    return jsonify(new_event), 201


if __name__ == "__main__":
    app.run(debug=True)