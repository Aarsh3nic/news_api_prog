import smtplib,ssl
import os

def send_email_news(news):
    host ="smtp.gmail.com"
    port = 465

    username = "SendingEmail"
    password = "passwordOfYourAcc"  # os.getenv("PASSforsecondarygmail") can be used to get password from env variable

    receiver = "ReceivingEmail"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context = context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,news)
