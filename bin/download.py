import subprocess
import sys
# Download source files through locize CLI

project_id = str(sys.argv[len(sys.argv)-1].split('=')[len(sys.argv[len(sys.argv)-1].split('='))-1])
print('Project_id ===>', project_id)
subprocess.run('cd %s && locize download && cd ..' % project_id, shell=True)
