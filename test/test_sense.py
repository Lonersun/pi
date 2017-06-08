# -*- coding:utf-8 -*-
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pi_modules.sense import sense
from pi_modules.beep import beep

sense_server = sense.Sense(12)
result = sense_server.detct()
if result is True:
    beep_server = beep.Beep(21)
    print "附近有人"
    beep_server.interval_beep(5)
else:
    print "附近无人"
