import os

def run_docker_compose(port, path, path_to_db, path_to_app, name, run_down, do_build):
  os.environ["DYNAMIC_PORT"] = port
  os.environ["DYNAMIC_PATH_DB"] = path_to_db
  os.environ["DYNAMIC_PATH_APP"] = path_to_app
  build = ''
  if do_build:
    build = '--build'
  if run_down:
    os.system('docker-compose -f ' + path + ' -p ' + name + ' down -v')
  else:
    os.system('docker-compose -f ' + path + ' -p ' + name + ' up -d ' + build + ' --force-recreate')

def add_to_committer_report(path, timestamp, branch_name, merger_branch_name, pusher):
  f = open(path + 'commits.txt', 'a')
  text = '[ ' + timestamp + ' ] ' + pusher + ' merged to ' + branch_name + ' from ' + merger_branch_name + '\\n'
  f.write(text)
  f.close()