from flask_restful import Resource, fields, marshal_with

from puffin.core import applications


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
        print(app_list)
        return app_list
