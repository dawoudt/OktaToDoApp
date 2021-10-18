# my_app/authentication.py
from django.contrib.auth import get_user_model
from rest_framework import authentication
from rest_framework import exceptions

from api import okta


class OktaAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        if bearer_token := request.META.get('HTTP_AUTHORIZATION', None):
            if okta.is_access_token_valid(bearer_token):
                jwt = okta.parse_token(bearer_token)
                email = jwt[1]['sub']
                user, _ = get_user_model().objects.get_or_create(email=email)
                return (user, None) # authentication successful
        return None
