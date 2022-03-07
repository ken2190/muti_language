class BaseConfig():
    DEBUG = False
    JSON_AS_ASCII = False
    RESTFUL_JSON = dict(ensure_ascii=False)


class DevConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@192.168.1.65:3306/test?charset=utf8'
    # 自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True


config = DevConfig
