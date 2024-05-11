import os
from flask import Flask, redirect, request
import requests

app = Flask(__name__)


@app.route("/sendemail", methods=["POST"])
def handle_send_email():
    """
    This function emulates traditional (1990s) handling of form POST requests.
    """
    send_email(request.form.get("message"), request.form.get("email"))
    return redirect("http://www.christianisaman.com")


def send_email(message, user):
    mailgun_domain = os.getenv("MAILGUN_DOMAIN")

    return requests.post(
        f"https://api.mailgun.net/v3/{mailgun_domain}/messages",
        auth=("api", os.getenv("MAILGUN_API_KEY")),
        data={
            "from": f"Mailgun Sandbox <mailgun@{mailgun_domain}>",
            "to": [os.getenv("MAIL_INBOX")],
            "subject": "New website message!",
            "text": f"{message}\n\nSender: {user}",
        },
    )


if __name__ == "__main__":
    import os
    from dotenv import load_dotenv
    load_dotenv()
    app.run(debug=True, port=5001)
