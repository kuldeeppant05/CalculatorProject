import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

def send_email(sender_email, receiver_email,subject,body,password,smtp_server="smtp.gmail.com",smtp_port=587):
    message =MIMEMultipart()
    message['From']=sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body,'plain'))

    with smtplib.SMTP (smtp_server,smtp_port) as server:
        server.starttls()
        server.login(sender_email,password)
        server.sendmail((sender_email,receiver_email,message.as_string()))
        print("Email sent")

sender_email="kuldeeppant@gmail.com"
receiver_email="avantu10@icloud.com"
subject="Test Email"
body="Hello Awantu"
password=""

send_email(sender_email,receiver_email,subject,body,password)



