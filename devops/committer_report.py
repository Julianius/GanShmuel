from mailing import send_email 
from config import DYNAMIC_PATH

TLD_DEVOPS = 'shekel8@gmail.com'
TLD_WEIGHT = 'yael260640@gmail.com'
TLD_BILLING = 'ravivnadiv2@gmail.com'
TLD_HELPER = 'vjulianiusv@gmail.com'
PATH = '/home/ec2-user/GanShmuel/app/commits.txt'

def send_committer_report():
    text = ''
    with open(PATH, 'r') as reader:
        line = reader.readline()
        text += line
    send_email('Committer report', text, None, None, [TLD_DEVOPS, TLD_BILLING, TLD_WEIGHT, TLD_HELPER])

send_committer_report()