import smtplib, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(message, user):
    user = user or "anonymous"
    email = os.getenv("MAIL_USERNAME")
    body = f"{message}\n\nSender: {user}"

    msg = MIMEMultipart("alternative")
    msg["Subject"] = "New website message!"
    msg["From"] = email
    msg["To"] = os.getenv("MAIL_USERNAME")
    msg.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP(os.getenv("MAIL_SERVER"), 587)
    server.starttls()
    server.login(email, os.getenv("MAIL_PASSWORD"))
    server.sendmail(email, email, msg.as_string())
    server.quit()
