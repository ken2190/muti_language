from han.app import db

# from app.model.movie import Movie

session = db.session


def movie_list(page, skip):
    default_page = 20
    default_skip = 0
    if page is None:
        page = default_page
    if skip is None:
        skip = default_skip
    # movie = session.query(Movie)[page * skip, page * (skip + 1)]
    # return movie.toString()
    mock = {
        "list": [
            {
                "address": "https:www.baidu.com",
                "ctime": "2021-09-01",
                "id": 1,
                "name": "第一部",
                "opnic": "https: www.baidu.com",
                "utime": "2021-09-01"
            },
            {
                "address": "https: www.baidu.com",
                "ctime": "2021-09-01",
                "id": 2,
                "name": "第二部",
                "opnic": "https: www.baidu.com",
                "utime": "2021-09-01"
            },
            {
                "address": "https: www.baidu.com",
                "ctime": "2021-09-01",
                "id": 3,
                "name": "第三部",
                "opnic": "https: www.baidu.com",
                "utime": "2021-09-01"
            }
        ]
    }
    return mock
