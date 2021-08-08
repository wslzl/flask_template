from flask import Blueprint, jsonify, request
from app import db
from app.models import User

users = Blueprint('user', __name__)


@users.route('/user-list', methods=['GET'])
def user_list():
    users_list = User.query.first()
    return jsonify(users_list.get_schema())


@users.route('/update-user', methods=['POST'])
def update_user():
    data = request.form
    name = data.get("name")
    up_user = User.query.filter(User.name == name).first()
    up_user.age += 1
    db.session.commit()
    return {}


@users.route('/add-user', methods=['POST'])
def add_user():
    data = request.form
    name = data.get("name")
    age = data.get("age")
    new_user = User(name=name, age=age)
    db.session.add(new_user)
    db.session.commit()
    return {"data": 200, "msg": "success"}