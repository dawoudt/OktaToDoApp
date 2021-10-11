import asyncio
import json
from django.conf import settings
from okta_jwt_verifier import JWTVerifier


loop = asyncio.get_event_loop()


def get_okta_config():
    return (
        settings.OKTA_CONFIG['VUE_APP_OKTA_DOMAIN'],
        settings.OKTA_CONFIG['VUE_APP_OKTA_CLIENT_ID']
    )

def is_access_token_valid(token, issuer=None, client_id=None):
    """
    Token: Bearer Token from Header
    issuer: Okta Domain
    client: client_id from okta
    """
    issuer, client_id = get_okta_config()

    jwt_verifier = JWTVerifier(issuer, client_id, 'api://default')
    try:
        loop.run_until_complete(jwt_verifier.verify_access_token(token))
        return True
    except Exception:
        return False


def is_id_token_valid(token, issuer, client_id, nonce):
    jwt_verifier = JWTVerifier(issuer, client_id, 'api://default')
    try:
        loop.run_until_complete(jwt_verifier.verify_id_token(token, nonce=nonce))
        return True
    except Exception:
        return False