# data.py
# In-memory list of events
events = [
    {"id": 1, "title": "Meeting"},
    {"id": 2, "title": "Workshop"}
]

def get_all_events():
    """Return all events"""
    return events

def add_event(title):
    """Add a new event with unique ID"""
    new_id = len(events) + 1
    new_event = {"id": new_id, "title": title}
    events.append(new_event)
    return new_event