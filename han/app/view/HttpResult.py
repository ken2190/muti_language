import json

from han.app import CustomizeError


class HttpResult:

    def __init__(self, data=None, message=None, code=200, success=True):
        # self.code = code,
        # self.sussess = success,
        # self.data = data,
        # self.message = message
        self.response = {
            "success": success,
            "code": code,
            "data": data,
            "message": message
        }

    @staticmethod
    def success(data=None, message=None, code=10000, success=True):
        res = HttpResult(data, message, code, success).response
        result = json.dumps(res, default=lambda o: o.__dict__, ensure_ascii=False)
        return result

    @staticmethod
    def failure(code, data=None, message=None, success=True):
        res = HttpResult(data, message, code, success).response
        result = json.dumps(res, default=lambda o: o.__dict__, ensure_ascii=False)
        return result

    @staticmethod
    def res(data=None, message=None, success=True):
        if message is isinstance(CustomizeError):
            return HttpResult.failure(10001, data, message, success)
        return HttpResult.success(data, message, success)
