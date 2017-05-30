# -*- coding:utf-8 -*-
import os

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
from pi_modules import config as pi_config
from pi_modules.digital import digital
from pi_modules.temperature import htu

htc_server = htu.HTU21D()
digital_server = digital.Digital()
while True:

    temperature = htc_server.readTemperatureData()
    humidity = htc_server.readHumidityData()
    print "当前温度：{0}, 湿度：{1}".format(temperature, humidity)
    digital_server.show_temperature(temperature, humidity)
    time.sleep(5)





