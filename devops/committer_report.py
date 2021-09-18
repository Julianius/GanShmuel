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