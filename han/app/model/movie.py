from han.app import db


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer(11), primary_key=True)
    name = db.Column(db.String(64), comment="电影名")
    opnic = db.Column(db.String(150), comment="影片剧照")
    address = db.Column(db.String(150), comment="电影地址")
    ctime = db.Column(db.Time, comment="抓取时间", default="2021-09-01")
    utime = db.Column(db.Time, comment="更新时间", default="2021-09-01")

    def toString(self):
        data = {
            'id': self.id,
            'name': self.name,
            'opnic': self.opnic,
            'address': self.address,
            'ctime': self.ctime,
            'utime': self.utime
        }
        return data


if __name__ == '__main__':
    movie = Movie(name="哈哈", opnic="https:www.baidu.com", address="https:www.baidu.com")
    db.session.addall(movie)
    db.session.commit
    pass
