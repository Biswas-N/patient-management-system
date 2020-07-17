import json
import os
from dotenv import load_dotenv
from flask import request
from functools import wraps
from jose import jwt
from jose.exceptions import JWTError
from urllib.request import urlopen

load_dotenv()
AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")
API_AUDIENCE = os.getenv("API_AUDIENCE")
ALGORITHMS = ["RS256"]


class AuthError(Exception):
    """
    AuthError (inheriting from Exception)
        A standardized way to communicate auth failure to endpoints
    """
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


def get_token_auth_header():
    """
    get_token_auth_header()
        Extracts the bearer token from an auth header (if in a correct
        format) or aborts with a 401

    @Output: a jwt object (dict) containing information like permission
        and user's email address
    TODO: Check if the return object's skeleton is correct
    """
    # Check if request has an Authorization header
    if 'Authorization' not in request.headers:
        raise AuthError({
            "code": "auth_header_not_found",
            "description": "Auth header needed"
        }, 401)

    auth_header = request.headers.get('Authorization')
    auth_header_arr = auth_header.split(' ')

    # Checking if we have the correct auth header (bearer token)
    if len(auth_header_arr) != 2:
        raise AuthError({
            "code": "auth_header_invalid",
            "description": "Invalid auth header"
        }, 401)
    elif auth_header_arr[0].lower() != "bearer":
        raise AuthError({
            "code": "auth_header_invalid",
            "description": "Invalid auth header"
        }, 401)
    else:
        return auth_header_arr[1]


def check_permissions(permission, payload):
    """
    check_permissions(permission, payload)
        Checks if the user has permission to access an endpoint

    @Input permission: string permission (i.e. 'post:drink')
    @Input payload: decoded jwt payload (dict)

    @Output:
        True - If permission exists in payload['permissions']
        Raises 400 - If permissions does not exists in payload
        Raises 401 - If permissions list exists in payload, but given
                     permission not in payload['permissions']
    """
    if "permissions" not in payload:
        raise AuthError({
            "code": "invalid_claims",
            "description": "Permissions not included in JWT"
        }, 400)
    elif permission not in payload['permissions']:
        raise AuthError({
            "code": "unauthorized",
            "description": "Permissions not found"
        }, 401)
    else:
        return True


def verify_decode_jwt(token):
    """
    verify_decode_jwt(token)
        Verifies the token authenticity by accessing the public key form
        auth0 service

    @Input token: a json web token (string)

    @Output:
        payload - (dict) containing the permissions and basic
        info of the user
        Raises 400 - If public key to decode the token cannot be accessed or
            could not decode or authenticate the token
        Raises 401 - If JWT token is invalid or
            Token expired or
            Incorrect API_AUDIENCE and AUTH0_DOMAIN details
    """
    jsonurl = urlopen(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')
    jwks = json.loads(jsonurl.read())

    try:
        unverified_header = jwt.get_unverified_header(token)
    except JWTError:
        raise AuthError({
            'code': 'invalid_jwt',
            'description': 'JWT token is invalid.'
        }, 401)

    rsa_key = {}
    if 'kid' not in unverified_header:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Authorization malformed.'
        }, 401)

    for key in jwks['keys']:
        if key['kid'] == unverified_header['kid']:
            rsa_key = {
                'kty': key['kty'],
                'kid': key['kid'],
                'use': key['use'],
                'n': key['n'],
                'e': key['e']
            }
    if rsa_key:
        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer='https://' + AUTH0_DOMAIN + '/'
            )

            return payload

        except jwt.ExpiredSignatureError:
            raise AuthError({
                'code': 'token_expired',
                'description': 'Token expired.'
            }, 401)

        except jwt.JWTClaimsError:
            raise AuthError({
                'code': 'invalid_claims',
                'description': 'Incorrect claims. Please, check the audience and issuer.'
            }, 401)
        except Exception:
            raise AuthError({
                'code': 'invalid_header',
                'description': 'Unable to parse authentication token.'
            }, 400)
    raise AuthError({
        'code': 'invalid_header',
        'description': 'Unable to find the appropriate key.'
    }, 400)


def requires_auth(permission=''):
    """
    requires_auth(permission='')
        Decorator to wrap any endpoint and apply middleware to check
        authentication and authorization

    @Input permission: string permission (i.e. 'post:drink')
    @Output
        True (payload as the first argument) - If the user has required
            permissions to access an endpoint
        Raises 400, 401 or 403 - Following the exceptions from
            get_token_auth_header(), verify_decode_jwt() and
            check_permissions()
    """
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = get_token_auth_header()
            payload = verify_decode_jwt(token)
            check_permissions(permission, payload)
            return f(payload, *args, **kwargs)

        return wrapper

    return requires_auth_decorator
