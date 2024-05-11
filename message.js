document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('messageForm').addEventListener('submit', function(event) {
        event.preventDefault();
        sendEmail();
    });
});

function sendEmail() {
    console.log('Sending email...');
    const name = document.getElementById('name').value;
    const message = document.getElementById('message').value;

    const formData = new URLSearchParams();
    formData.append('name', name);
    formData.append('message', message);

    // Specify the full URL to your Flask endpoint
    fetch('127.0.0.1:5000/sendemail', {
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
