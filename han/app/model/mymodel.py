from han.app import db


class User(db.Model):
    __tablename__ = 'user'
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(255))
    image = db.Column(db.String(255))
    role_id = db.Column(db.Integer, db.ForeignKey('db_roles.rid'))


class Role(db.Model):
    __tablename__ = 'db_roles'
    rid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship("User", backref="role")


if __name__ == '__main__':
    user1 = User(name='Tom', email='tom@163.com', password='123456', image='/upload/img-0000.jpg')
    user2 = User(name='Jack', email='jack@163.com', password='654321', image='/upload/img-0000.jpg')
    user3 = User(name='lili', email='lili@163.com', password='345678', image='/upload/img-0000.jpg')
    user4 = User(name='Pack', email='pack@163.com', password='964152', image='/upload/img-0000.jpg')

    db.session.add_all([user1, user2, user3, user4])
    db.session.commit()
