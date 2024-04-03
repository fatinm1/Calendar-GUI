function showCalendar() {
    const year = document.getElementById('year').value;
    if (year) {
        // Use a simple function to generate the calendar (placeholder)
        const calendarOutput = document.getElementById('calendarOutput');
        calendarOutput.innerHTML = `Calendar for ${year}`;
        // In a real application, you might generate the calendar here
    }
}

function addNote() {
    const date = prompt("Enter date (dd/mm):");
    const note = prompt("Enter note:");
    if (date && note) {
        // Store the note in localStorage or a global variable
        localStorage.setItem(date, note);
        alert(`Note for ${date} saved.`);
    }
}

function checkNote() {
    const date = prompt("Enter date (dd/mm) to check note:");
    if (date) {
        const note = localStorage.getItem(date);
        if (note) {
            alert(`Note for ${date}: ${note}`);
        } else {
            alert(`No note for ${date}.`);
        }
    }
}

// Add an event listener to check notes. This function is not directly linked in the HTML example above,
// but could be invoked through another UI element or process.
