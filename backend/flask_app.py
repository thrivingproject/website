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
    return redirect(os.getenv("FRONTEND_SERVER_DOMAIN"))


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
    from os import path
    from dotenv import load_dotenv

    env_file = path.join(path.dirname(path.realpath(__file__)), "env/.env")

    load_dotenv(env_file)

    app.run(debug=True, port=5001)
