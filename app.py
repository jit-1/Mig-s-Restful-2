from flask import Flask 
from flask.ext.restful import Api, Resource

app = Flask(__name__)
api = Api(App)

class TaskListAPI(Resource):
    def get(self):
        pass

    def post(self):
        pass

class TaskAPI(Resource):
    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass

api.add_resource(TaskListAPI, '/todo/api/v1.0/tasks', endpoint = 'tasks')
api.add_resource(TaskAPI, '/todo/api/v1.0/tasks/<int:id>', endpoint = 'task')