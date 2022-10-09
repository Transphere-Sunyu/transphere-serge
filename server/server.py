from flask import Flask, request
from util import GenerateConfFile
import subprocess
app = Flask(__name__)

# Run serge sync shell command
def serge_sync():
    return subprocess.run('serge sync', shell=True)

@app.route("/push", methods=['POST'])
def publish():
    args = request.args.to_dict()
    try:
        open(args['project_id']+'.serge','r')
        # serge_sync()
    except:
        print('Configuration file for project %s does not exists' % args['project_id'])
        print('Creating Configuration file for project %s' % args['project_id'])
        conf_file = GenerateConfFile.GenerateConfigurationFile(
            project_Id=int(args['project_id']),
            remote_path=args['remote_path'],
            # branch=args['branch'],
            task_id=args['task_id'],
            # source_language=args['source_language'],
            source_dir=args['source_dir'],
            # source_match=args['source_match'],

        )
        conf_file.write_file()
        # serge_sync()

    return '', 200


if __name__ == '__main__':
    app.run()
