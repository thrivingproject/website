document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('messageForm').addEventListener('submit', function(event) {
        event.preventDefault();
        sendEmail();
    });
});

function sendEmail() {
    const name = document.getElementById('name').value;
    const message = document.getElementById('message').value;

    const formData = new URLSearchParams();
    formData.append('name', name);
    formData.append('message', message);

    // Specify the full URL to your Flask endpoint
    fetch('http://example-backend.com/api/sendemail', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Failed to send email.');
    });
}
