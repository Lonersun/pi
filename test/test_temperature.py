# -*- coding:utf-8 -*-
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

"""
+  : 3.3v
GND: 接地
SDA: 3
SCL: 5

sudo i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: 40 -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
"""

from pi_modules.temperature import htu

htc_server = htu.HTU21D()
user = htc_server.readUserRegister()
temperature = htc_server.readTemperatureData()
humidity = htc_server.readHumidityData()
print "当前温度：{0}, 湿度：{1}".format(temperature, humidity)

