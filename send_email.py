import smtplib
import ssl
import os


def send_email(sender, text):
    host = os.getenv('HOST')
    port = 465
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
