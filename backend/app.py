from flask import Flask, redirect, request
from send_email import send_email
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


if __name__ == "__main__":
    app.run(debug=True, port=5001)
