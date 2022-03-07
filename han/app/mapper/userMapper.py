from han.app import db
from han.app.model.mymodel import User, Role


def get_user_by_id(id):
    return User.query.get(id)


def get_user_by_name(name):
    return User.query.filter(User.name == name).first()


def add_user(username, password):
    user = User(name=username, password=password)
    db.session.add(user)
    return db.session.commit()


def getusers():
    return User.query.all()


def getusersbyrid(rid):
    return User.query.filter(User.role_id == rid).all()


def getroles():
    roles = Role.query.all()
    return roles
