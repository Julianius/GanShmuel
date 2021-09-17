import smtplib
from mailing import send_email 
from config import DYNAMIC_PATH

TLD_DEVOPS = 'shekel8@gmail.com'
TLD_WEIGHT = 'yael260640@gmail.com'
TLD_BILLING = 'ravivnadiv2@gmail.com'
PATH = DYNAMIC_PATH + 'app/'

def send_committer_report():
    text = ''
    with open(PATH + 'commits.txt', 'r') as reader:
        line = reader.readline()
        text += line
    send_email('Committer report', text, None, None, [TLD_DEVOPS, TLD_BILLING, TLD_WEIGHT])

send_committer_report()


#def send_email():
#    sender_email = "bluedevopsdeveleap@gmail.com"
    #rec_email = [TLD_DEVOPS, TLD_BILLING, TLD_WEIGHT, 'vjulaniusv@gmail.com']
#    rec_email = [TLD_DEVOPS]
#    password = "blue123!"
#    text = ''
#    with open(PATH + 'commits.txt', 'r') as reader:
#        line = reader.readline()
#        text += line
    #print(text)
    #print('text')
    #f = open(PATH + 'commits.txt', 'r')
    #text = '[ ' + timestamp + ' ] ' + pusher + ' merged to ' + branch_name + ' from ' + merger_name
    #text = f.read()
    #f.close()
#    message = 'Subject: {}\n\n{}'.format('Committer Report', text)
#    server = smtplib.SMTP('smtp.gmail.com', 587)
#    server.starttls()
#    server.login(sender_email, password)
#    print("Login success")
#    server.sendmail(sender_email, rec_email, message)
#    print("Email has been sent to ", rec_email)

#send_email()