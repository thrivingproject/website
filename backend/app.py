import os
import requests
from flask import Flask, redirect, request
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()


@app.route("/sendemail", methods=["POST"])
def handle_send_email():
    """
    This function emulates traditional (1990s) handling of form POST requests.
    """
    send_email(request.form.get("message"), request.form.get("email"))
    return redirect("http://localhost:3000/")


# TODO: Implement the following function when using paid pythonanywhere
# def send_email(message, user):
#     user = user or "anonymous"
#     email = os.getenv("MAIL_USERNAME")
#     body = f"{message}\n\nSender: {user}"

#     msg = MIMEMultipart("alternative")
#     msg["Subject"] = "New website message!"
#     msg["From"] = email
#     msg["To"] = os.getenv("MAIL_USERNAME")
#     msg.attach(MIMEText(body, "plain"))

#     server = smtplib.SMTP(os.getenv("MAIL_SERVER"), 587)
#     server.connect(os.getenv("MAIL_SERVER"), 587)  # Explicitly connect to the server
#     server.ehlo()  # Identify yourself to an ESMTP server using EHLO
#     server.starttls()
#     server.ehlo()  # After starttls, you need to say EHLO again
#     server.login(email, os.getenv("MAIL_PASSWORD"))
#     server.sendmail(email, email, msg.as_string())
#     server.quit()


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
    app.run(debug=True, port=5001)
