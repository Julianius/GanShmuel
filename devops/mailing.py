import smtplib
from config import *

SENDER_EMAIL = 'develeapblueteum@gmail.com'
PASSWORD = 'blue123!'
SERVER_NAME = 'smtp.gmail.com'
SERVER_CODE = 587

def send_email(subject, text, team_leader = None, pusher = None, rec_emails = None):
    if rec_emails == None:
        if team_leader == pusher:
            rec_emails = [team_leader]
        else:
            rec_emails = [team_leader,pusher]

    message = 'Subject: {}\n\n{}'.format(subject, text)
    server = smtplib.SMTP(SERVER_NAME, SERVER_CODE)
    server.starttls()
    server.login(SENDER_EMAIL, PASSWORD)
    print('Login success')
    server.sendmail(SENDER_EMAIL, rec_emails, message)
    print('Email has been sent to ', rec_emails)