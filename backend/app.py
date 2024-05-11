from flask import Flask, redirect, request
import send_email

app = Flask(__name__)


@app.route("/sendemail", methods=["POST"])
def handle_send_email():
    """
    This function emulates traditional (1990s) handling of form POST requests.
    """
    form = request.form
    print(form)
    user_message = form.get("message")
    user_email = form.get("email")
    print(user_message, user_email)
    # send_email(user_message)
    return redirect('http://localhost:3000/')


if __name__ == "__main__":
    app.run(debug=True, port=5001)
