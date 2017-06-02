# -*- coding:utf-8 -*-
import requests
from ..utils import json_utils


class TuLingRobot(object):
    """
    图灵机器人
    """

    def __init__(self, api_key, secret, url='http://www.tuling123.com/openapi/api'):
        self.api_key = api_key
        self.secret = secret
        self.url = url

    def exchange_info(self, info):
        """
        获取机器人信息
        :param info:
        :return:
        """
        content = info.decode('utf-8')
        params = {
            'key': self.api_key,
            'info': content
        }
        result = requests.get(self.url, params)
        if result.status_code != 200:
            return {'code': 500001, 'text': u'服务器好像挂掉了'}
        return result.json()
