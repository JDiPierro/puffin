import flask

from flask_restful import Resource, fields, marshal_with, marshal

from puffin.rest import auth
from puffin.core import applications, docker
from puffin.core.security import get_user
from puffin.rest.util import ApplicationStatusField


class ApplicationListResource(Resource):
    application_list_fields = {
        'application_id': fields.String,
        'name': fields.String,
        'subtitle': fields.String,
        'logo': fields.String
    }

    @marshal_with(application_list_fields)
    def get(self):
        app_list = applications.get_application_list()
        return app_list


class ApplicationInformationResource(Resource):
    """
    Information about an Application
    """
    application_metadata_fields = {
        'application_id': fields.String(attribute='application.application_id'),
        'name': fields.String(attribute='application.name'),
        'subtitle': fields.String(attribute='application.subtitle'),
        'logo': fields.String(attribute='application.logo'),
        'description': fields.String(attribute='application.description'),
        'image_version': fields.String,
    }
    
    @marshal_with(application_metadata_fields)
    def get(self, application_id):
        application = applications.get_application(application_id)
        if not application:
            flask.abort(404)
        client = docker.get_client()
        image_version = docker.get_application_image_version(client, application)
        
        return {
            'application': application,
            'image_version': image_version
        }


class RunningApplicationResource(Resource):
    """
    Information about a running instance of an application.
    """
    method_decorators = [auth.login_required]
    running_application_fields = {
        'application_id': fields.String(attribute='application.application_id'),
        'running_version': fields.String,
        'domain': fields.String,
        'image_version': fields.String,
        'status': ApplicationStatusField
    }
    
    @marshal_with(running_application_fields)
    def get(self, application_id):
        application = applications.get_application(application_id)
        if not application:
            flask.abort(404)
        
        client = docker.get_client()
        current_user = get_user(auth.username())
        
        image_version = docker.get_application_image_version(client, application)
        application_status = docker.get_application_status(client, current_user, application)
        running_version = docker.get_application_version(client, current_user, application)
        domain = applications.get_application_domain(current_user, application)
        
        return {
            'application': application,
            'status': application_status,
            'image_version': image_version,
            'running_version': running_version or "Unknown",
            'domain': domain
        }