from han.app import LoginError
from han.app.mapper.userMapper import get_user_by_name, get_user_by_id


def login(values):
    name = values.get("name")
    password = values.get("password")
    if not name:
        return LoginError("账号不能为空")
    elif not password:
        return LoginError("密码不能为空")
    else:
        user = get_user_by_name(name)
        if user and user.password == password:
            return "登录成功"
        else:
            return LoginError(" 用户名或密码错误")


def getuser(id):
    return get_user_by_id(id)


def register(values):
    # if getuserbyName(values.get("name")):
    #     return "账户已存在"
    # else:
    #     username = values.get("name")
    #     password = values.get("password")
    #     if addUser(username, password):
    #         return "注册成功"
    #     return "注册失败"
    username = values.get("name")
    password = values.get("password")
    return "{},{}{}".format(username, password, "注册成功")
