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
MESSAGE_SUCCESS = 'All tests passedd successfully! System is running and operational.'
HEADING_FAILURE = 'team tests failure'
MESSAGE_FAILURE = 'Some tests have failed. Please check!'