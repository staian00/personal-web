import smtplib
import ssl
from dotenv import load_dotenv
import os


def configure():
    load_dotenv()


def send_email(sender, text):
    configure()
    host = os.getenv('HOST')
    port = int(os.getenv('PORT'))
    username = os.getenv('USER')
    password = os.getenv('PASSWORD')
    receiver = os.getenv('RECEIVER')
    context = ssl.create_default_context()
    message = f'''\
Subject: Personal Page - {sender}
{text}
'''
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
