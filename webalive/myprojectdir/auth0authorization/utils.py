# auth0authorization/utils.py

from django.contrib.auth import authenticate

# auth0authorization/utils.py

import json
import jwt
import requests

def jwt_decode_token(token):
    header = jwt.get_unverified_header(token)
    jwks = requests.get('https://{}/.well-known/jwks.json'.format('webalive.us.auth0.com')).json()
    public_key = None
    for jwk in jwks['keys']:
        if jwk['kid'] == header['kid']:
            public_key = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(jwk))

    if public_key is None:
        raise Exception('Public key not found.')

    issuer = 'https://{}/'.format('webalive.us.auth0.com')
    return jwt.decode(token, public_key, audience='YOUR_API_IDENTIFIER', issuer=issuer, algorithms=['RS256'])

def jwt_get_username_from_payload_handler(payload):
    username = payload.get('sub').replace('|', '.')
    authenticate(remote_user=username)
    return username