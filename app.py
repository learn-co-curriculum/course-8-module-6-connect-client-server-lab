from flask import Flask, jsonify, request  # type: ignore[reportMissingImports]

app = Flask(__name__)

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
    data = request.get_json(silent=True) or {}
    title = data.get("title")
    
    if not title or not str(title).strip():
        return jsonify({"error": "Title is required"}), 400

    new_id = max((e["id"] for e in events), default=0) + 1
    new_event = {"id": new_id, "title": str(title).strip()}
    events.append(new_event)  # Fixed: changed products.append to events.append
    
    return jsonify(new_event), 201

if __name__ == "__main__":
    app.run(debug=True)