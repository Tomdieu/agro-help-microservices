import requests
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed


class TokenAuthentication(BaseAuthentication):

    def authenticate(self, request):

        token = request.headers.get('Authorization')
        if not token:
            return None

        # Here we are going to a request to the auth service

        response = requests.get(
            'http://account_service:8001/api/account/validate-token/', headers={'Authorization': token})
        if response.status_code != 200:
            raise AuthenticationFailed({'detail': 'Invalid token'})

        # Extract the user from the response and set in the request
        user = response.json().get('user')
        request.user = user

        return (user, None)
