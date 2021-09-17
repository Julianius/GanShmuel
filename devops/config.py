import os

DYNAMIC_PATH = str(os.environ.get('DYNAMIC_PATH'))
REPO = 'https://github.com/Julianius/GanShmuel.git'
SUCCESS_CODE = 0
FAILURE_CODE = 1
PATH_APP = '/GanShmuel/app/'
PATH_TEST = '/GanShmuel/test/'
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