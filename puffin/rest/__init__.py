from flask_httpauth import HTTPBasicAuth
from flask_security.utils import verify_password

from puffin import app
from puffin.core.security import get_user

auth = HTTPBasicAuth()

@auth.verify_password
def api_verify_password(username, password):
    user = get_user(username)
    if user:
        return verify_password(password, user.password)
    return False


from flask_restful import Api

from puffin.rest.resources import RootResource
from puffin.rest.resources.application import \
    ApplicationListResource, \
    ApplicationInformationResource, \
    RunningApplicationResource


api = Api(app)

api.add_resource(RootResource, '/')
api.add_resource(ApplicationListResource, '/applications')
api.add_resource(ApplicationInformationResource, '/applications/<string:application_id>')
api.add_resource(RunningApplicationResource, '/applications/<string:application_id>/status')