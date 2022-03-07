from flask import Blueprint, request

project = Blueprint("project", __name__)


class Interface_:
    def __init__(self, method, url,
                 params=None, data=None, headers=None, cookies=None, files=None,
                 auth=None, timeout=None, allow_redirects=True, proxies=None,
                 hooks=None, stream=None, verify=None, cert=None, json=None):
        self.method = method
        pass
