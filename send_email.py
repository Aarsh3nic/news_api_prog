import smtplib,ssl
import os

def send_email_news(news):
    host ="smtp.gmail.com"
    port = 465

    username = "5mindisc@gmail.com"
    password = os.getenv("PASSforsecondarygmail")  # getting environment variable

    receiver = "5mindisc@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context = context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,news)