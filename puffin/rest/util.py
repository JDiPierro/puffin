from flask_restful import fields

from puffin.core.applications import ApplicationStatus


class ApplicationStatusField(fields.Raw):
    def format(self, value):
        """
        DELETED = 0
        CREATED = 10
        UPDATING = 20
        ERROR = 90
        """
        if value == ApplicationStatus.DELETED:
            return "DELETED"
        elif value == ApplicationStatus.CREATED:
            return "CREATED"
        elif value == ApplicationStatus.UPDATING:
            return "UPDATING"
        elif value == ApplicationStatus.ERROR:
            return "ERROR"
