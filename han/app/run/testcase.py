import json

from pip._vendor import requests
from pip._vendor.requests import Request


class BaseModel:
    def __setitem__(self, key, value):
        print("调用了__setitem__")
        super().__setattr__(key, value)  # 等价于object.__setattr__(self, key, value) 内部使调用setattr()实现

        # self[item]读取会调用此方法
        # 这里是重写dict.__getitem__方法

    def __getitem__(self, item):
        print("调用了__getitem__")
        return super().__getattribute__(item)


# class Request(BaseModel):
#     def __init__(self, method, url,
#                  params=None, data=None, headers=None, cookies=None, files=None,
#                  auth=None, timeout=None, allow_redirects=True, proxies=None,
#                  hooks=None, stream=None, verify=None, cert=None, json=None):
#         self.method = method
#         pass


class TestCase(BaseModel):
    def __init__(self, name, requset: Request, setup_hooks=None, teardown_hooks=None):
        self.name = name
        self.requset = requset
        self.setup_hooks = setup_hooks
        self.teardown_hooks = teardown_hooks


if __name__ == '__main__':
    # case_requset = {
    #     "name": "请求1",
    #     "url": "/testcase/1"
    # }
    res = Request(method="POST", url="/asaa/ss", data="{'ss':'ss'}")

    case = TestCase("haha", res.__dict__)
    print(json.dumps(case.__dict__, ensure_ascii=False))
    pass
