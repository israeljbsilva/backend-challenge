from rest_framework import exceptions
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    """ Overriding Django rest framework's custom exception """
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:

        if isinstance(exc, (exceptions.NotAuthenticated, exceptions.PermissionDenied)):
            return response

        if not isinstance(exc, exceptions.APIException):
            response.data['status_code'] = response.status_code
    return response
