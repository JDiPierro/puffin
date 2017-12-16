from flask_restful import Api

from puffin import app
from puffin.rest.resources.application import ApplicationListResource


api = Api(app)

api.add_resource(ApplicationListResource, '/applications')