from han.app import db


class Project(db.Model):
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)


if __name__ == '__main__':
    pro1 = Project(name="工程1")
    pro2 = Project(name="工程2")
    pro3 = Project(name="工程3")

    db.session.add_all([pro1, pro2, pro3])
    db.session.commit()
