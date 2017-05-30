# -*- coding:utf-8 -*-
import os

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pi_modules import config as pi_config
from pi_modules.digital.digital import show_date, show_temperature, show_time
from pi_modules.temperature import htu

htc_server = htu.HTU21D()
user = htc_server.readUserRegister()
temperature = htc_server.readTemperatureData()
humidity = htc_server.readHumidityData()

show_temperature(temperature, humidity)





