import subprocess
import sys
# Upload source files through starling CLI

project_id = str(sys.argv[len(sys.argv)-1].split('=')[len(sys.argv[len(sys.argv)-1].split('='))-1])
print('Project_id ===>', project_id)
subprocess.run('cd %s && starling client upload && cd ..' % project_id, shell=True)
