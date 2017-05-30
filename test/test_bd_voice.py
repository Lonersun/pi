# -*- coding:utf-8 -*-
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pi_modules.voice import bd_voice
from pi_modules import config as pi_config

bd_voice_server = bd_voice.BaiDuVoice(pi_config.BD_UID, pi_config.BD_API_KEY, pi_config.BD_SECRET_KEY)

# 语音输出
# content = "尉老师"
# result = bd_voice_server.voice_mix(content)
# print result


result = bd_voice_server.voice_text("/tmp/2017-05-27_14_35_41.wav")
print result
