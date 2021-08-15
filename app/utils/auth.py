from flask import request, g, jsonify
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired, BadSignature
from functools import wraps
from config import Config


def generate_token(user, expiration=24*60*60):
    s = Serializer(Config.SECRET_KEY, expires_in=expiration)
    token = s.dumps({
        "id": user['id'],
        "username": user['username'],
    }).decode("utf-8")
    return token


def verify_token(token):
    s = Serializer(Config.SECRET_KEY)
    try:
        data = s.loads(token)
    except (BaseException, SignatureExpired):
        return None
    return data


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization', None)
        if token:
            string_token = token.encode('ascii', 'ignore')
            user = verify_token(string_token)
            if user:
                g.current_user = user
                return f(*args, **kwargs)
        return jsonify(msg="Auth is required"), 401
    return decorated
