# Events Catalog

## Overview

Events Catalog is a lightweight web application that demonstrates how to connect a front end built with HTML and JavaScript to a Flask-powered back end. The application uses the Fetch API to communicate with Flask endpoints, allowing users to retrieve and add events without refreshing the page.

This project showcases the fundamentals of client-server communication, JSON data exchange, and dynamic DOM updates.

## Features

* View a list of events retrieved from the Flask back end.
* Add new events through a form.
* Display newly added events immediately without reloading the page.
* Exchange data between the client and server using JSON.
* Validate user input before submitting requests.

## Technologies Used

* Python
* Flask
* HTML5
* CSS3
* JavaScript (Fetch API)

## Project Structure

```text
events-catalog/
│
├── server.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   ├── script.js
│   └── style.css
└── README.md
```

## API Endpoints

### GET /

Returns a welcome message in JSON format.

**Response**

```json
{
  "message": "Welcome!"
}
```

---

### GET /events

Returns all events stored in the application.

**Example Response**

```json
[
  {
    "id": 1,
    "title": "Yoga in the Park"
  },
  {
    "id": 2,
    "title": "Lake 5K Run"
  }
]
```

---

### POST /events

Creates a new event.

**Request Body**

```json
{
  "title": "Community Cleanup"
}
```

**Successful Response**

```json
{
  "id": 3,
  "title": "Community Cleanup"
}
```

If the request does not include a title or the title is empty, the server returns an error response with an appropriate HTTP status code.

## Installation

1. Clone the repository.

```bash
git clone git@github.com:wanja-juma/course-8-module-6-connect-client-server-lab.git
```

2. Navigate to the project directory.

```bash
cd events-catalog
```

3. (Optional) Create and activate a virtual environment.

**Linux/macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

4. Install the project dependencies.

```bash
pip install -r requirements.txt
```

## Running the Application

Start the Flask development server.

```bash
python server.py
```

The application will be available at:

```text
http://127.0.0.1:5000
```

## How It Works

1. The client sends a **GET** request to retrieve the list of events.
2. Flask returns the events as JSON.
3. JavaScript dynamically renders the events on the page.
4. When a user submits the form, JavaScript validates the input.
5. A **POST** request containing JSON is sent to the server.
6. Flask processes the request, stores the new event in memory, and returns the newly created event.
7. JavaScript immediately updates the page by displaying the new event.

## Testing

Run the automated tests with:

```bash
pytest
```

The tests verify that:

* The welcome endpoint returns a successful JSON response.
* The events endpoint returns a list of events.
* New events can be added successfully.
* Invalid event submissions return an appropriate error response.

## Future Improvements

* Persist events using a database such as SQLite or PostgreSQL.
* Add the ability to edit and delete events.
* Include event dates, locations, and descriptions.
* Improve the user interface with enhanced styling and responsive design.
* Deploy the application using a production-ready WSGI server.
