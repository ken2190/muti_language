MYSQL_CONFIG = {
    "host": "handev-w.mysql.rds.aliyuncs.com",
    "user": "hanbook",
    "password": "IOaBLTXo9FN54VwyP3wJ",
    "database": "han_hanbook",
    "port": 3306,
    "charset": "utf8"
}


# MYSQL_CONFIG = {
#     "host": "192.168.1.65",
#     "user": "root",
#     "password": "123456",
#     "database": "test",
#     "port": 3306,
#     "charset": "utf8"
# }


class User(object):
    def __setitem__(self, key, value):
        print("调用了__setitem__")
        super().__setattr__(key, value)  # 等价于object.__setattr__(self, key, value) 内部使调用setattr()实现

    # self[item]读取会调用此方法
    # 这里是重写dict.__getitem__方法
    def __getitem__(self, item):
        print("调用了__getitem__")
        return super().__getattribute__(item)




