from flask import Blueprint, jsonify, request
from ..utils.auth import generate_token, requires_auth, verify_token

login = Blueprint('login', __name__)


@login.route('/login', methods=['POST'])
def logins():
    try:
        user_info = request.form
    except Exception:
        user_info = {}
    if not user_info:
        user_info = {}
    print(user_info)
    username = user_info["username"]
    password = user_info["password"]
    user = {
        "id": 1,
        "password": username,
        "password": password
    }
    if username == 'admin' and password == '123':
        return jsonify(token=generate_token({
        "id": 1,
        "username": username,
        "password": password
    }))
    return jsonify(code=403, msg="error")


@login.route('/auth_login', methods=['GET'])
@requires_auth
def auth_login():
    return {'xx': 1}
