import os

DYNAMIC_PATH = str(os.environ.get('DYNAMIC_PATH'))
REPO = 'https://github.com/Julianius/GanShmuel.git'
SUCCESS_CODE = 0
FAILURE_CODE = 1

PATH_APP = '/GanShmuel/app/'
PATH_TEST = '/GanShmuel/test/'
WEIGHT='Weight'
BILLING='Billing'
STAGE='Stage'
MAIN='Main'
DEVOPS='Devops'
BRANCHES_ALLOWED = [ 'main', 'weight-staging', 'billing-staging' ]
BRANCHES_FORBIDDEN = [ 'devops', 'weight', 'billing' ]

DOCKER_COMPOSE_PATHS = { 
  'weight': '/weight/docker-compose.yml',
  'billing': '/billing/Prod/docker-compose.yml'
}

APPS_DB_PATHS = {
  'weight': DYNAMIC_PATH + 'app/weight-staging/weight',
  'billing': DYNAMIC_PATH + 'app/billing-staging/billing/Prod'
}

APPS_PATHS = {
  'weight': DYNAMIC_PATH + 'app/weight-staging/weight',
  'billing': DYNAMIC_PATH + 'app/billing-staging/billing/Prod'
}

TEST_APPS_DB_PATHS = {
  'weight': DYNAMIC_PATH + 'test/weight-staging/weight',
  'billing': DYNAMIC_PATH + 'test/billing-staging/billing/Prod'
}

TEST_APPS_PATHS = {
  'weight': DYNAMIC_PATH + 'test/weight-staging/weight',
  'billing': DYNAMIC_PATH + 'test/billing-staging/billing/Prod'
}

HEADING_SUCCESS = 'team tests success'
MESSAGE_SUCCESS = 'All tests passedd successfully!'
HEADING_FAILURE = 'team tests failure'
MESSAGE_FAILURE = 'Some tests have failed. Please check!'

HEADING_SUCCESS_DEPLOY = 'team deploy success'
MESSAGE_SUCCESS_DEPLOY = 'System has been deployed successfully! System is running and operational.'
HEADING_FAILURE_DEPLOY = 'team deploy failure'
MESSAGE_FAILURE_DEPLOY = 'System was not deployed successfully. Please check!'

CONTACT_EMAILS = {
    "weight_team": {
        "Julianius": "julianmotorbreathe@gmail.com",
        "yaelkadosh": "yael260640@gmail.com",
        "Faresbad": "fares.badran@studio.unibo.it",
        "sapsap1": "sapiralon95@gmail.com",
        "shaygman": "shaygman@gmail.com",
        "Yoav Yung": "joaffzie@gmail.com"
    },

    "billing_team": {
        "Julianius": "julianmotorbreathe@gmail.com",
        "nadivravivz": "ravivnadiv2@gmail.com",
        "naorsavorai": "naorsv@gmail.com",
        "af176": "abigail.f176@gmail.com",
        "kfirosb": "kfirosb@gmail.com"
    },

    "devops_team": {
        "matanshk": "shekel8@gmail.com",
        "Julianius": "julianmotorbreathe@gmail.com",
        "Izhak": "izhaklatovski@gmail.com"
    }
}

SWITCHER_STAGING_WEIGHT=1
SWITCHER_STAGING_BILLING=1
SWITCHER_MAIN_BILLING=1
SWITCHER_MAIN_WEIGHT=1