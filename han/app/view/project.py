import sqlalchemy
from flask import Blueprint, request
from flask_restful import marshal, fields

from han.app.view.HttpResult import HttpResult

project = Blueprint("project", __name__)

project_fields = {
    "id": fields.Integer,
    "name": fields.String
}


@project.route("/all")
def all():
    from han.app.model.ProjectDao import Project
    prj = Project.query.all()
    prj_str = marshal(prj, project_fields, envelope="projects")
    res = HttpResult.success(prj_str)
    return res


@project.route("/info/<id>")
def info(id):
    from han.app.model.ProjectDao import Project
    prj = Project.query.get(id)
    prj_str = marshal(prj, project_fields, envelope="projects")
    res = HttpResult.success(prj_str)
    return res


@project.route("/add", methods=["POST"])
def add():
    from han.app.model.ProjectDao import Project
    from han.app import db
    if request.values:
        name = request.values.get("name")
        project = Project(name=name)
        try:
            db.session.add(project)
        except sqlalchemy.exc.IntegrityError as e:
            return HttpResult.success(message="添加失败")
        db.session.commit()
        return HttpResult.success(message="添加成功")
    return HttpResult.success(message="参数不能为空")


#
# @project.route("/del")
# def delete():
#     return "delProject"
#
#
# @project.route("/update")
# def update():
#     return "updateProject"


if __name__ == '__main__':
    pass
