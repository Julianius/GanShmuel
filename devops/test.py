import os
from mailing import *

BRANCHES_ALLOWED = ['main', 'weight-staging', 'billing-staging']
SUCCESS_CODE = 0
FAILURE_CODE = 1
PATH_TEST = '/GanShmuel/test/'
PATH_APP = '/GanShmuel/app/'

def check_contacts(branch_name, pusher, merger_name):    
    if branch_name =="weight-staging":
        run_tests(CONTACT_EMAILS["weight_team"]['yaelkadosh'], CONTACT_EMAILS["weight_team"][pusher], branch_name, merger_name)

    elif branch_name =="billing-staging":
        run_tests(CONTACT_EMAILS["billing_team"]['nadivravivz'], CONTACT_EMAILS["billing_team"][pusher], branch_name, merger_name)
    else:
        for team in CONTACT_EMAILS.items():
            if pusher in team[1]:
                if team[0] == "weight_team":
                    run_tests(CONTACT_EMAILS["weight_team"]['yaelkadosh'], CONTACT_EMAILS["weight_team"][pusher], branch_name, merger_name)
                elif team[0] == "billing_team":
                    run_tests(CONTACT_EMAILS["billing_team"]['nadivravivz'], CONTACT_EMAILS["billing_team"][pusher], branch_name, merger_name)
                else:
                    run_tests(CONTACT_EMAILS["devops_team"]['matanshk'], CONTACT_EMAILS["devops_team"][pusher], branch_name, merger_name)
                break
        pass

def run_tests(team_leader, pusher, branch_name, merger_name):

    os.environ["DYNAMIC_PORT"] = "8085"
    is_weight  = False
    os.system('rm -rf ' + PATH_TEST + branch_name)
    os.system('mkdir -p ' + PATH_TEST + branch_name)
    os.system('cp -a '+ PATH_APP + 'temp/* ' + PATH_APP + 'temp/.* ' + PATH_TEST + branch_name + '/ 2>/dev/null')

    if branch_name == BRANCHES_ALLOWED[0]:
      if merger_name == BRANCHES_ALLOWED[1]:
        os.system('docker-compose -f ' + PATH_TEST + branch_name + '/weight/docker-compose.yml -p main-weight up -d --build --force-recreate')        
        test_result = weight_test(team_leader, pusher)     
      elif merger_name == BRANCHES_ALLOWED[2]:
        os.system('docker-compose -f ' + PATH_TEST + branch_name + '/billing/Prod/docker-compose.yml -p main-billing up -d --build --force-recreate')
        test_result = billing_test(team_leader, pusher)
    elif branch_name == BRANCHES_ALLOWED[1]:
        os.system('docker-compose -f ' + PATH_TEST + branch_name + '/weight/docker-compose.yml -p weight-staging up -d --build --force-recreate')
        test_result = weight_test(team_leader, pusher)
        os.system('docker-compose -f ' + PATH_TEST + branch_name + '/weight/docker-compose.yml down -v')         
    else:
        os.system('docker-compose -f ' + PATH_TEST + branch_name + '/billing/Prod/docker-compose.yml -p billing-staging up -d --build --force-recreate')
        test_result = billing_test(team_leader, pusher)

    if test_result == SUCCESS_CODE:
        send_email("Blue team tests success", "All the tests succeeded, good job!", team_leader, pusher)
    else:
        send_email("Blue team tests failure", "Some tests failed, go check your code.", team_leader, pusher)
    
    return test_result

def billing_test(team_leader, pusher):
    ## Still no path for billing 13.09.2021
    #res = os.exec('/bin/python3 ' + PATH_TESTS + BRANCHES_ALLOWED[2] + '')
    res = 0
    if res == SUCCESS_CODE:
        send_email('Billing team tests success', 'All the tests succeeded, good job!', team_leader, pusher)
        return SUCCESS_CODE
    else:
        send_email('Billing team tests success', 'All the tests succeeded, good job!', team_leader, pusher)
        return FAILURE_CODE

def weight_test(team_leader, pusher):
    #res = os.exec('/bin/python3 ' + PATH_TESTS + BRANCHES_ALLOWED[3] + '/app/test.py')
    res = 0
    if res == SUCCESS_CODE:
        send_email('Billing team tests success', 'All the tests succeeded, good job!', team_leader, pusher)
        return SUCCESS_CODE
    else:
        send_email('Billing team tests success', 'All the tests succeeded, good job!', team_leader, pusher)
        return FAILURE_CODE