import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(message):
    sender_email = "your-email@gmail.com"  # Your email
    receiver_email = "your-email@example.com"  # Your email, or where you want to receive messages
    password = "your-password"  # Your email account password

    msg = MIMEMultipart("alternative")
    msg["Subject"] = "New Contact Form Message"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    text = "You received a message from {}: {}".format(name, message)
    part1 = MIMEText(text, "plain")

    msg.attach(part1)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()