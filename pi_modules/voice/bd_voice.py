# -*- coding:utf-8 -*-
import requests
from urllib import urlencode
import uuid
import subprocess
import audio

from ..utils.cache_helper import memcached


class BaiDuVoice(object):

    text2voice_cgi = "http://tsn.baidu.com/text2audio"
    oauth_cgi = "https://openapi.baidu.com/oauth/2.0/token/"
    voice2text_cgi = 'http://vop.baidu.com/server_api'

    def __init__(self, uid, api_key, secret_key):
        self.uid = uid
        self.api_key = api_key
        self.secret_key = secret_key
        self.session = requests.Session()

    def set_access_token(self):
        """

        :return:
        """
        url = self.oauth_cgi + "?grant_type=client_credentials&client_id={0}&client_secret={1}".format(self.api_key,
                                                                                                       self.secret_key)
        result = self.session.get(url)
        if result.status_code != 200:
            return False
        # 解析数据
        data = result.json()
        # 存入memcache
        memcached.add("bd_voice_access_token", data.get('access_token'), timeout=int(data.get('expires_in')))
        return data.get('access_token')

    def get_access_token(self):
        """

        :return:
        """
        access_token = memcached.get("bd_voice_access_token")
        if not access_token:
            return self.set_access_token()
        return access_token

    def voice_mix(self, content):
        access_token = self.get_access_token()
        if len(bytes(content)) > 1000:
            content = "文字太多了，我读不过来！"
        spec = {
            'tex': content,
            'lan': 'zh',
            'tok': access_token,
            'ctp': 1,
            'cuid': str(uuid.uuid4()),
            'spd': 5,
            'pit': 5,
            'vol': 8,
            'per': 0
        }
        url_get = self.text2voice_cgi + "?" + urlencode(spec)
        # subprocess.call(["mplayer", url_get], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.call(["mplayer", url_get], shell=False, stdout=None, stderr=subprocess.PIPE)

    def voice_text(self, file_str=""):
        """
        语音转汉字
        :param file_str:
        :return:
        """
        access_token = self.get_access_token()
        if file_str is None or len(file_str) == 0:
            return None
        # 读取音频文件
        audio_server = audio.AudioModule()
        data, f_len = audio_server.get_wav_data(file_str=file_str)
        spec = {
            'cuid': str(uuid.uuid4()),
            'token': access_token
        }
        url = self.voice2text_cgi + '?' + urlencode(spec)
        headers = {
            'Content-Type': 'audio/pcm; rate=8000',
            'Content-Length': '%d' % f_len
        }
        response = self.session.post(url=url, headers=headers, data=data)
        data = response.json()
        if data.get('err_no') != 0:
            return "语音解析失败"
        return data.get('result')[0]
