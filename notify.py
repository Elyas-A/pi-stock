import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv
load_dotenv()


def send_notification(subject: str, body: str) -> None:
    """
    send an email notification to the user

    parameters: subject - str, required
                          subject of the email
                body - str, required
                       body of the email
    """
    # construct message
    message = EmailMessage()
    message.set_content(body)
    message["from"] = os.getenv("SENDER_EMAIL")
    message["subject"] = subject
    message["to"] = os.getenv("RECEIVER_EMAIL")

    # start up email server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(os.getenv("SENDER_EMAIL"), os.getenv("SENDER_PASSWORD"))

    # send email
    server.send_message(message)

    # stop the email server
    server.quit()
