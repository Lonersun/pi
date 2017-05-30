# -*- coding:utf-8 -*-
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pi_modules.beep import beep

beep_server = beep.Beep(21)
result = beep_server.interval_beep(0.5, 10)
print "蜂鸣结束"

