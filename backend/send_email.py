import smtplib, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(message, user):
    user = user or "anonymous"
    email = os.getenv("MAIL_USERNAME")

    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"New website message!"
    msg["From"] = email
    msg["To"] = os.getenv("MAIL_USERNAME")

    text = f"{message}\n\nSender: {user}"

    msg.attach(MIMEText(text, "plain"))
    print(msg.as_string(), msg)

    server = smtplib.SMTP(os.getenv("MAIL_SERVER"), 587)
    server.starttls()
    server.login(email, os.getenv("MAIL_PASSWORD"))
    server.sendmail(email, email, msg.as_string())
    server.quit()
