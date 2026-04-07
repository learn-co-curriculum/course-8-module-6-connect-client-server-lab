# simple in-memory list of events
events = [
    {"id": 1, "title": "Meeting"},
    {"id": 2, "title": "Workshop"}
]


# function to get all events
def get_all_events():
    return events


# function to add a new event
def add_event(title):
    # create new id
    new_id = len(events) + 1

    new_event = {
        "id": new_id,
        "title": title
    }

    events.append(new_event)

    return new_event