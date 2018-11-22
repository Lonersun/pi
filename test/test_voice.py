# -*- coding:utf-8 -*-
import os

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pi_modules import config as pi_config
from pi_modules.voice import audio, bd_voice, tuling

audio_server = audio.AudioModule()
bd_voice_server = bd_voice.BaiDuVoice(pi_config.BD_UID, pi_config.BD_API_KEY, pi_config.BD_SECRET_KEY)
tuling_server = tuling.TuLingRobot(pi_config.TULING_API_KEY, pi_config.TULING_API_SECRET)

print "==>开始运行...."
print "==>录音"
result = audio_server.record_wave()
print result
print "==>转换音频为文本"
result = bd_voice_server.voice_text(result)
print result
print "==>唤起机器人"
result = tuling_server.exchange_info(result)
print result.get('text')
print "==>转换为语音，进行输出"
result = bd_voice_server.voice_mix(result.get('text'))
print "==>运行完毕"





