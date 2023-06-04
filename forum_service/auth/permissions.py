import requests
from rest_framework.permissions import BasePermission


class TokenPermission(BasePermission):
    def has_permission(self, request, view):
        # Get the token from the request headers
        token = request.headers.get('Authorization')

        # Make an HTTP request to validate the token
        response = requests.get(
            'http://account_service:8001/validate-token', headers={'Authorization': token})

        # Check the response to see if the token is valid
        if response.status_code == 200:
            return True
        else:
            return False
