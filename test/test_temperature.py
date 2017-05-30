# -*- coding:utf-8 -*-
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pi_modules.temperature import htu

htc_server = htu.HTU21D()
user = htc_server.readUserRegister()
temperature = htc_server.readTemperatureData()
humidity = htc_server.readHumidityData()
print "当前温度：{0}, 湿度：{1}".format(temperature, humidity)

