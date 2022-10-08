from flask import Flask, request
from util import GenerateConfFile

app = Flask(__name__)


@app.route("/push", methods=['POST'])
def publish():
    args = request.args.to_dict()
    conf_file = GenerateConfFile.GenerateConfigurationFile(
        project_Id=int(args['project_id']),
        remote_path=args['remote_path'],
        branch=args['branch'],
        task_id=args['task_id'],
        # source_language=args['source_language'],
        source_dir=args['source_dir'],
        # source_match=args['source_match'],

    )
    conf_file.write_file()

    return '', 200


if __name__ == '__main__':
    app.run()
