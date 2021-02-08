import requests
from requests.auth import HTTPBasicAuth

from config import TestConfig


def hit_endpoint(type, request_url, auth=None, data=None, headers=None, json=None, timeout=None):
    if auth is None:
        auth = HTTPBasicAuth(TestConfig.username, TestConfig.password)

    if type in 'get':
        response = requests.get(request_url, auth=auth, data=data, headers=headers, json=json,
                                timeout=timeout)
    elif type in 'post':
        response = requests.post(request_url, auth=auth, data=data, headers=headers, json=json,
                                 timeout=timeout)
    elif type in 'delete':
        response = requests.delete(request_url, auth=auth, data=data, headers=headers, json=json,
                                   timeout=timeout)
    elif type in 'put':
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        response = requests.put(request_url, auth=auth, data=data, headers=headers, json=json,
                                timeout=timeout)
    elif type in 'patch':
        response = requests.patch(request_url, auth=auth, data=data, headers=headers, json=json,
                                  timeout=timeout)
    else:
        raise Exception('Cannot understand request type')

    return response


def alert_profile_template():
    return {
      "name": "string",
      "orgId": 3398,
      "categoryType": "Path",
      "attribs": [
        {
          "id": 0,
          "param": "string",
          "scope": "string",
          "overInterval": 0,
          "underInterval": 0,
          "value": 0
        }
      ]
    }