import smtplib
# from typing import Counter


def check_contacts(BRANCH_NAME,PUSHER):
    PUSHER_EMAILS={
        "weight_team":{
            "matanshk":"shekel8@gmail.com",
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
        run_tests(PUSHER_EMAILS["weight_team"]['yaelkadosh'],PUSHER_EMAILS["weight_team"][PUSHER])

    elif BRANCH_NAME =="billing-staging":
        run_tests(PUSHER_EMAILS["billing_team"]['nadivravivz'],PUSHER_EMAILS["billing_team"][PUSHER])
    else:
        #need to write the same for main branch
        pass


def send_email(SUBJECT, TEXT, TEAM_LEADER, PUSHER):
    sender_email = "bluedevopsdeveleap@gmail.com"
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
    with open("test.txt", "r") as test_file:
        file_read=test_file.readlines()
        failure_list=[]
        counter=0
        for line in file_read:
            counter+=1
            test_result=int(line.split(">")[-1].split(" ")[1])
            num=int(line[1])
            result=num%2
            # If current test is successful, move on
            if (result==0 and test_result==0) or (result==1 and test_result==1):
                pass
            # If current test failed, add its number to the failure list
            else:
                failure_list.append(counter)
                
        # Send success email
        if len(failure_list)==0:
            send_email("Blue team tests success", "All the tests succeeded, good job!", TEAM_LEADER, PUSHER)
            return 0
        # Send failure email
        else:
            send_email("Blue team tests failure", "Following tests failed: " + str(failure_list), TEAM_LEADER, PUSHER)
            return 1

check_contacts("weight-staging","matanshk")
#run_tests("shekel8@gmail.com", "email@gmail.com",)