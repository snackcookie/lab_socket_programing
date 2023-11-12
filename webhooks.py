from flask import Flask, json
from flask_restful import Resource, Api

import os

buildBranch = 'main'
buildPath = '/mnt/c/Users/dlals/OneDrive/바탕 화면/github_webhook_python/lab_socket_programing'

buildCommand = 'cd' + buildPath + ' && git stash && git pull origin '

app = Flask(__name__)
api = Api(app)

class setDeploy(Resource):
    def post(self):
        os.system(buildCommand)
        return {'status' : 'success'}
    
api.add_resource(setDeploy, '/deploy')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
