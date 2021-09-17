import os
from mailing import *
from utils import *
from config import *

TESTING_PORT = '8085'

def check_contacts(branch_name, pusher, merger_name):    
    if branch_name =="weight-staging":
        result = run_tests(CONTACT_EMAILS["weight_team"]['yaelkadosh'], CONTACT_EMAILS["weight_team"][pusher], branch_name, merger_name)

    elif branch_name =="billing-staging":
        result = run_tests(CONTACT_EMAILS["billing_team"]['nadivravivz'], CONTACT_EMAILS["billing_team"][pusher], branch_name, merger_name)
    else:
        for team in CONTACT_EMAILS.items():
            if pusher in team[1]:
                if team[0] == "weight_team":
                    result = run_tests(CONTACT_EMAILS["weight_team"]['yaelkadosh'], CONTACT_EMAILS["weight_team"][pusher], branch_name, merger_name)
                elif team[0] == "billing_team":
                    result = run_tests(CONTACT_EMAILS["billing_team"]['nadivravivz'], CONTACT_EMAILS["billing_team"][pusher], branch_name, merger_name)
                else:
                    result = run_tests(CONTACT_EMAILS["devops_team"]['matanshk'], CONTACT_EMAILS["devops_team"][pusher], branch_name, merger_name)
                break
    return result

def run_tests(branch_name, merger_name):
    os.system('rm -rf ' + PATH_TEST + branch_name)
    os.system('mkdir -p ' + PATH_TEST + branch_name)
    os.system('cp -a '+ PATH_APP + 'temp/* ' + PATH_APP + 'temp/.* ' + PATH_TEST + branch_name + '/ 2>/dev/null')

    if branch_name == BRANCHES_ALLOWED[0]:
        if merger_name == BRANCHES_ALLOWED[1]:
            run_docker_compose(TESTING_PORT, PATH_TEST + branch_name + DOCKER_COMPOSE_PATHS['weight'], APPS_DB_PATHS['weight'], APPS_PATHS['weight'], 'test-weight-main', False, True)
            test_result = weight_test()
            run_docker_compose(TESTING_PORT, PATH_TEST + branch_name + DOCKER_COMPOSE_PATHS['weight'], APPS_DB_PATHS['weight'], APPS_PATHS['weight'], 'test-weight-main', True, False)
        elif merger_name == BRANCHES_ALLOWED[2]:
            run_docker_compose(TESTING_PORT, PATH_TEST + branch_name + DOCKER_COMPOSE_PATHS['billing'], APPS_DB_PATHS['billing'], APPS_PATHS['billing'], 'test-billing-main', False, True)
            test_result = billing_test()
            run_docker_compose(TESTING_PORT, PATH_TEST + branch_name + DOCKER_COMPOSE_PATHS['billing'], APPS_DB_PATHS['billing'], APPS_PATHS['billing'], 'test-billing-main', True, False)
    elif branch_name == BRANCHES_ALLOWED[1]:
        run_docker_compose(TESTING_PORT, PATH_TEST + branch_name + DOCKER_COMPOSE_PATHS['weight'], APPS_DB_PATHS['weight'], APPS_PATHS['weight'], 'test-weight-staging', False, True)
        test_result = weight_test()
        run_docker_compose(TESTING_PORT, PATH_TEST + branch_name + DOCKER_COMPOSE_PATHS['weight'], APPS_DB_PATHS['weight'], APPS_PATHS['weight'], 'test-weight-staging', True, False)
    else:
        run_docker_compose(TESTING_PORT, PATH_TEST + branch_name + DOCKER_COMPOSE_PATHS['billing'], APPS_DB_PATHS['billing'], APPS_PATHS['billing'], 'test-billing-staging', False, True)
        test_result = billing_test()
        run_docker_compose(TESTING_PORT, PATH_TEST + branch_name + DOCKER_COMPOSE_PATHS['billing'], APPS_DB_PATHS['billing'], APPS_PATHS['billing'], 'test-billing-staging', True, False)
    return test_result

def billing_test():
    #os.environ["FLASK_APP"] = PATH_TEST + BRANCHES_ALLOWED[2] + '/Test/test.py'
    #res = os.system('flask run')#   bin/python3 ' + PATH_TEST + BRANCHES_ALLOWED[2] + '/Test/test.py')
    #os.system('sleep 10')
    res = os.system('python3 ' + PATH_TEST + BRANCHES_ALLOWED[2] + '/billing/Test/billing_test.py')
    #res = 0
    if res == SUCCESS_CODE:
        #send_email('Billing team tests success', 'All the tests succeeded, good job!', team_leader, pusher)
        return SUCCESS_CODE
    else:
        #send_email('Billing team tests success', 'All the tests succeeded, good job!', team_leader, pusher)
        return FAILURE_CODE

def weight_test():
    #res = os.exec('/bin/python3 ' + PATH_TESTS + BRANCHES_ALLOWED[3] + '/app/test.py')
    #os.system("chmod +x test.py")
    res = os.system('python3 ' + PATH_TEST + BRANCHES_ALLOWED[1] + '/weight/app/test.py')
    #res = 0
    if res == SUCCESS_CODE:
        #send_email('Billing team tests success', 'All the tests succeeded, good job!', team_leader, pusher)
        return SUCCESS_CODE
    else:
        #send_email('Billing team tests success', 'All the tests succeeded, good job!', team_leader, pusher)
        return FAILURE_CODE