import smtplib, os
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


def run_tests(TEAM_LEADER, PUSHER, BRANCH_NAME,MERGER_NAME):

    ##### docker compose up (test compose) - START
    PATH = '/GanShmuel/test/'
    os.environ["DYNAMIC_PORT"] = "8085"
    BRANCHES_ALLOWED = ['main', 'weight-staging', 'billing-staging']
    if BRANCH_NAME == BRANCHES_ALLOWED[0]:
      if MERGER_NAME == BRANCHES_ALLOWED[1]:
        os.system('docker-compose -f ' + PATH + BRANCH_NAME + '/weight/docker-compose.yml -p main-weight up -d --build --force-recreate')
        
        ### weight test
        test_result = billingtest() ## <----- WEIGHT TEST FILE
        if test_result == 0:
            send_email("Weight team tests success", "All the tests succeeded, good job!", TEAM_LEADER, PUSHER)
            return 0
        elif test_result == 1:
            send_email("Weight team tests failure", "Some tests failed, go check your code.", TEAM_LEADER, PUSHER)
            return 1
        ### end weight test

      elif MERGER_NAME == BRANCHES_ALLOWED[2]:
        os.system('docker-compose -f ' + PATH + BRANCH_NAME + '/billing/Prod/docker-compose.yml -p main-billing up -d --build --force-recreate')

        ### billing test
        test_result = billingtest() ## <----- billing TEST FILE
        if test_result == 0:
            send_email("Billing team tests success", "All the tests succeeded, good job!", TEAM_LEADER, PUSHER)
            return 0
        elif test_result == 1:
            send_email("Billing team tests failure", "Some tests failed, go check your code.", TEAM_LEADER, PUSHER)
            return 1

        ### end billing test

    elif BRANCH_NAME == BRANCHES_ALLOWED[1]:
        os.system('docker-compose -f ' + PATH + BRANCH_NAME + '/weight/docker-compose.yml -p weight-staging up -d --build --force-recreate')
    
        ### weight test
        test_result = billingtest() ## <----- WEIGHT TEST FILE
        if test_result == 0:
            send_email("Weight team tests success", "All the tests succeeded, good job!", TEAM_LEADER, PUSHER)
            return 0
        elif test_result == 1:
            send_email("Weight team tests failure", "Some tests failed, go check your code.", TEAM_LEADER, PUSHER)
            return 1
        ### end weight test
    
    else:
        os.system('docker-compose -f ' + PATH + BRANCH_NAME + '/billing/Prod/docker-compose.yml -p billing-staging up -d --build --force-recreate')
            ### billing test
        test_result = billingtest() ## <----- billing TEST FILE
        if test_result == 0:
            send_email("Billing team tests success", "All the tests succeeded, good job!", TEAM_LEADER, PUSHER)
            return 0
        elif test_result == 1:
            send_email("Billing team tests failure", "Some tests failed, go check your code.", TEAM_LEADER, PUSHER)
            return 1

        ### end billing test
    ##### docker compose up (test compose) - end



    test_result = billingtest()
    if test_result == 0:
        send_email("Blue team tests success", "All the tests succeeded, good job!", TEAM_LEADER, PUSHER)
        return 0
    elif test_result == 1:
        send_email("Blue team tests failure", "Some tests failed, go check your code.", TEAM_LEADER, PUSHER)
        return 1

# Entrypoint
check_contacts("main","Izhak")