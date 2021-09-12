import smtplib
# from typing import Counter

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


run_tests("mail@gmail.com", "email@gmail.com")