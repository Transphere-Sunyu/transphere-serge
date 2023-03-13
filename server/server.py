import subprocess
import time
import threading
import os

# TODO: use environment variables

ACCESS_KEY = os.environ.get('STARLING_AK')
SECRET_KEY = os.environ.get('STARLING_SK')


# Run serge sync
def serge_sync():
    return subprocess.run('serge sync ../data/configs/ >../log/serge.log 2>&1', shell=True)


# Run serge clean-ts command
def serge_clean():
    return subprocess.run('serge clean-ts ../data/configs/ >>../log/serge.log 2>&1', shell=True)


def serge_loop():
    while True:
        serge_sync()
        serge_clean()

        print("Waiting 10 seconds till the next cycle. Press [Ctrl+C] to stop...")
        time.sleep(10)


serge = threading.Thread(target=serge_loop)
serge.start()
