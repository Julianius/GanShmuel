import smtplib

CONTACT_EMAILS = {
    "weight_team": {
        "Julianius": "julianmotorbreathe@gmail.com",
        "yaelkadosh": "yael260640@gmail.com",
        "Faresbad": "fares.badran@studio.unibo.it",
        "sapsap1": "sapiralon95@gmail.com",
        "shaygman": "shaygman@gmail.com",
        "Yoav Yung": "joaffzie@gmail.com"
    },

    "billing_team": {
        "Julianius": "julianmotorbreathe@gmail.com",
        "nadivravivz": "ravivnadiv2@gmail.com",
        "naorsavorai": "naorsv@gmail.com",
        "af176": "abigail.f176@gmail.com",
        "kfirosb": "kfirosb@gmail.com"
    },

    "devops_team": {
        "matanshk": "shekel8@gmail.com",
        "Julianius": "julianmotorbreathe@gmail.com",
        "Izhak": "izhaklatovski@gmail.com"
    }
}
SENDER_EMAIL = 'develeapblueteum@gmail.com'
PASSWORD = 'blue123!'
SERVER_NAME = 'smtp.gmail.com'
SERVER_CODE = 587

def send_email(subject, text, team_leader = None, pusher = None, rec_emails = None):
    rec_emails=['vjulianiusv@gmail.com']
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