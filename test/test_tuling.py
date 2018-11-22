# -*- coding:utf-8 -*-
import os
import sys
from urllib import quote
reload(sys)
sys.setdefaultencoding("utf-8")

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pi_modules.voice import bd_voice
from pi_modules import config as pi_config, tuling

a = tuling.TuLingRobot(pi_config.TULING_API_KEY, pi_config.TULING_API_SECRET)
result = a.exchange_info("讲个笑话")
text = result.get('text')
bd_voice_server = bd_voice.BaiDuVoice(pi_config.BD_UID, pi_config.BD_API_KEY, pi_config.BD_SECRET_KEY)

bd_voice_server.voice_mix(text)
