import http.client
import json
import urllib.parse

from .exception import ApiException


def get_error_message(message: str):
    message = json.loads(message)
    return message.get("message", "")


class Transport(object):

    def __init__(self, endpoint: str, token: str):
        self.token = token
        self.endpoint = endpoint
        self.connection = http.client.HTTPSConnection(self.endpoint)

    def get(self, path: str, param: dict):
        param["token"] = self.token
        query = urllib.parse.urlencode(param)
        print(f"{path}?{query}")
        self.connection.request("GET", f"{path}?{query}")
        response = self.connection.getresponse()
        if response.code < 400:
            return json.loads(response.read())
        else:
            message = get_error_message(response.read())
            raise ApiException(response.code, message)

    def post(self, path: str, param: dict):
        headers = {'Content-type': 'application/json'}
        body = json.dumps(param)
        self.connection.request("POST", path, body, headers)
        response = self.connection.getresponse()
        if response.code < 400:
            return json.loads(response.read())
        else:
            message = get_error_message(response.read())
            raise ApiException(response.code, message)
