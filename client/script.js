const eventList = document.querySelector("#event-list");
const form = document.querySelector("form");
const titleInput = document.querySelector("#title");

// Load existing events
fetch("/events")
  .then(response => response.json())
  .then(events => {
    events.forEach(renderEvent);
  })
  .catch(error => console.error(error));


// Submit new event
form.addEventListener("submit", (e) => {
    e.preventDefault();

    const title = titleInput.value.trim();

    // Client-side validation
    if (title === "") {
        alert("Please enter an event title.");
        return;
    }

    fetch("/events", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            title: title
        })
    })
    .then(response => response.json())
    .then(event => {
        renderEvent(event);
        form.reset();
    })
    .catch(error => console.error(error));
});


function renderEvent(event) {
    const li = document.createElement("li");
    li.textContent = event.title;
    eventList.appendChild(li);
}