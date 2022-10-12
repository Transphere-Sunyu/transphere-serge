from flask import Flask, request
from util import GenerateConfFile
import subprocess
import time
import threading
# app = Flask(__name__)

ACCESS_KEY = "AKLTMDc3MGY5ZmI4NDI4NDRjZmE0ZjkyMDhjZDQ0YzI0Yzg"
SECRET_KEY = "T0RReE1EQXlZMk0wWVdNMU5ETTBZVGhsTkdFd00yVmxPVGRsWkdRMll6VQ=="

# Run serge sync shell command
def serge_sync():
    return subprocess.run('cd ../bin  && serge sync', shell=True)

# Run serge clean-ts command
def serge_clean():
    return subprocess.run('cd ../bin  && serge clean-ts', shell=True)

def serge_loop():

        while True:

            serge_sync()
            serge_clean()

            print("Waiting 10 seconds till the next cycle. Press [Ctrl+C] to stop...")
            time.sleep(10)

serge = threading.Thread(target=serge_loop)
serge.start()

# if __name__ == '__main__':
#     app.run()
