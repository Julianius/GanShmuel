import smtplib
from billingtest import billingtest

def check_contacts(BRANCH_NAME,PUSHER):
    PUSHER_EMAILS={
        "weight_team":{
            "yaelkadosh":"yael260640@gmail.com",
            "Faresbad":"fares.badran@studio.unibo.it",
            "sapsap1":"sapiralon95@gmail.com",
            "shaygman":"shaygman@gmail.com",
            "Yoav Yung":"joaffzie@gmail.com"
        },

        "billing_team": {
            "nadivravivz":"ravivnadiv2@gmail.com",
            "naorsavorai":"naorsv@gmail.com",
            "af176":"abigail.f176@gmail.com",
            "kfirosb":"kfirosb@gmail.com",
        },

        "devops_team": {
            "matanshk":"shekel8@gmail.com",
            "Julianius":"julianmotorbreathe@gmail.com",
            "Izhak":"izhaklatovski@gmail.com",
        }}
        
    if BRANCH_NAME =="weight-staging":
        run_tests(PUSHER_EMAILS["weight_team"]['yaelkadosh'], PUSHER_EMAILS["weight_team"][PUSHER])

    elif BRANCH_NAME =="billing-staging":
        run_tests(PUSHER_EMAILS["billing_team"]['nadivravivz'], PUSHER_EMAILS["billing_team"][PUSHER])
    else:
        for team in PUSHER_EMAILS.items():
            if PUSHER in team[1]:
                if team[0] == "weight_team":
                    run_tests(PUSHER_EMAILS["weight_team"]['yaelkadosh'], PUSHER_EMAILS["weight_team"][PUSHER])
                elif team[0] == "billing_team":
                    run_tests(PUSHER_EMAILS["billing_team"]['nadivravivz'], PUSHER_EMAILS["billing_team"][PUSHER])
                else:
                    run_tests(PUSHER_EMAILS["devops_team"]['matanshk'], PUSHER_EMAILS["devops_team"][PUSHER])
                break
        pass


def send_email(SUBJECT, TEXT, TEAM_LEADER, PUSHER):
    sender_email = "bluedevopsdeveleap@gmail.com"
    if TEAM_LEADER == PUSHER:
        rec_email = [TEAM_LEADER]
    else:
        rec_email = [TEAM_LEADER,PUSHER]
    password = "blue123!"
    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    print("Login success")
    server.sendmail(sender_email, rec_email, message)
    print("Email has been sent to ", rec_email)


def run_tests(TEAM_LEADER, PUSHER):
    test_result = billingtest()
    if test_result == 0:
        send_email("Blue team tests success", "All the tests succeeded, good job!", TEAM_LEADER, PUSHER)
        return 0
    elif test_result == 1:
        send_email("Blue team tests failure", "Some tests failed, go check your code.", TEAM_LEADER, PUSHER)
        return 1

# Entrypoint
check_contacts("main","Izhak")