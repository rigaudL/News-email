import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_email(subject, message):
    sender_email = "Rigaudluly21@gmail.com"
    receiver_email = sender_email  # Replace with recipient email address
    password = os.getenv("Password")  # Use environment variable to store password

    # Create a multipart message and set headers
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    msg.attach(MIMEText(message, "plain"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
