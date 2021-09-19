import os
from mailing import *
from utils import *
import config

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
    print('rm -rf ' + PATH_TEST + branch_name)
    os.system('rm -rf ' + PATH_TEST + branch_name)
    print('mkdir -p ' + PATH_TEST + branch_name)
    os.system('mkdir -p ' + PATH_TEST + branch_name)
    print('cp -a '+ PATH_APP + 'temp/* ' + PATH_APP + 'temp/.* ' + PATH_TEST + branch_name + '/ 2>/dev/null')
    os.system('cp -a '+ PATH_APP + 'temp/* ' + PATH_APP + 'temp/.* ' + PATH_TEST + branch_name + '/ 2>/dev/null')

    print(BRANCHES_ALLOWED[0])
    print(BRANCHES_ALLOWED[1])
    print(BRANCHES_ALLOWED[2])
    print(merger_name)
    if branch_name == BRANCHES_ALLOWED[0]:
        print('HERE 1')
        if merger_name == BRANCHES_ALLOWED[1]:
            docker_compose_up(TESTING_PORT, PATH_TEST + branch_name + DOCKER_COMPOSE_PATHS['weight'], TEST_APPS_DB_PATHS['weight'], TEST_APPS_PATHS['weight'], str(config.SWITCHER_MAIN_WEIGHT) + 'main', True)
            test_result = weight_test()
            docker_compose_down(PATH_TEST + branch_name + DOCKER_COMPOSE_PATHS['weight'], 'test-weight-main')
        elif merger_name == BRANCHES_ALLOWED[2]:
            print('HERE 2')
            docker_compose_up(TESTING_PORT, PATH_TEST + branch_name + DOCKER_COMPOSE_PATHS['billing'], TEST_APPS_DB_PATHS['billing'], TEST_APPS_PATHS['billing'], str(config.SWITCHER_MAIN_BILLING) + 'main', True)
            test_result = billing_test()
            docker_compose_down(PATH_TEST + branch_name + DOCKER_COMPOSE_PATHS['billing'], 'test-billing-main')
    elif branch_name == BRANCHES_ALLOWED[1]:
        docker_compose_up(TESTING_PORT, PATH_TEST + branch_name + DOCKER_COMPOSE_PATHS['weight'], TEST_APPS_DB_PATHS['weight'], TEST_APPS_PATHS['weight'], str(config.SWITCHER_STAGING_WEIGHT) + 'staging', True)
        test_result = weight_test()
        docker_compose_down(PATH_TEST + branch_name + DOCKER_COMPOSE_PATHS['weight'], 'test-weight-staging')
    else:
        docker_compose_up(TESTING_PORT, PATH_TEST + branch_name + DOCKER_COMPOSE_PATHS['billing'], TEST_APPS_DB_PATHS['billing'], TEST_APPS_PATHS['billing'], str(config.SWITCHER_STAGING_BILLING) + 'staging', True)
        test_result = billing_test()
        docker_compose_down(PATH_TEST + branch_name + DOCKER_COMPOSE_PATHS['billing'], 'test-billing-staging')
    return test_result  

def billing_test():
    res = os.system('python3 ' + PATH_TEST + BRANCHES_ALLOWED[2] + '/billing/Test/test.py')
    #res = 0
    if res == SUCCESS_CODE:
        return SUCCESS_CODE
    else:
        return FAILURE_CODE

def weight_test():
    res = os.system('python3 ' + PATH_TEST + BRANCHES_ALLOWED[1] + '/weight/app/test.py')
    #res = 0
    if res == SUCCESS_CODE:
        return SUCCESS_CODE
    else:
        return FAILURE_CODE