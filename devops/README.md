Devops Branch
subprocess.call((
      'rm -rf ' + PATH + 'temp', 
      'git clone -b ' + branch_name + ' ' + REPO + ' ' + PATH + 'temp',  
      'rm -rf ' + PATH + branch_name,
      'mkdir -p ' + PATH + branch_name,
      'mv '+ PATH + 'temp/* ' + PATH + 'temp/.* ' + PATH + branch_name + '/ 2>/dev/null'
      'rm -rf ' + PATH + 'temp'
    ))