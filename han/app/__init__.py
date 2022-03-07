import logging
from flask import Flask, request, jsonify
from flask_restful import Api

from flask_sqlalchemy import SQLAlchemy

from han.app import config
from han.app.view.project import project
from han.app.view.user import user

app = Flask(__name__)
api = Api(app)
logger = logging.getLogger('app')


@app.route("/")
def index():
    return "index"


@app.route("/movie", methods=["POST"])
def movie():
    page = request.values.get("page")
    skip = request.values.get("skip")
    res = request.json
    from han.app.mapper.movieMapper import movie_list
    res = movie_list(page, skip)
    return jsonify(res)


app.register_blueprint(project, url_prefix="/project")
app.register_blueprint(user, url_prefix="/user")
app.config.from_object(config)
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run()
    pass
