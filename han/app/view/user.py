from flask import Blueprint, request
from flask_restful import fields, marshal

from han.app.view.HttpResult import HttpResult

user = Blueprint("user", __name__)

user_fields = {
    'uid': fields.Integer,  # integer代表数字
    'name': fields.String,  # String代表str
    'email': fields.String,  # 设置如果money无值默认为0
    'image': fields.String,  # 设置该字段重命名为lv
    'role_id': fields.Integer
}


@user.route("/register", methods=['POST'])
def register():
    from han.app.service.userService import register
    res = register(request.values)
    return HttpResult.success(res)


@user.route("/login", methods=['POST'])
def login():
    from han.app.service.userService import login
    res = login(request.values)
    return HttpResult.success(res)


@user.route("/info/<id>", methods=['GET'])
def info(id):
    from han.app.service.userService import getuser
    res = getuser(id)
    data = marshal(res, user_fields)
    return HttpResult.success(data)
