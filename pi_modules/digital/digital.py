# encoding: utf-8

import RPi.GPIO
import time
from pi_modules.temperature import htu


class Digital(object):
    
    def __init__(self):
        # 定义单个数码管各段led对应的GPIO口
        self.LED_A = 26
        self.LED_B = 19
        self.LED_C = 13
        self.LED_D = 6
        self.LED_E = 5
        self.LED_F = 11
        self.LED_G = 9
        self.LED_DP = 10
    
        # 定义1到4号数码管阳极对应的GPIO口
        self.DIGIT1 = 12
        self.DIGIT2 = 16
        self.DIGIT3 = 20
        self.DIGIT4 = 21
    
        # 定义按钮输入的GPIO口
        btn = 27
    
        RPi.GPIO.setmode(RPi.GPIO.BCM)
    
        RPi.GPIO.setup(self.LED_A, RPi.GPIO.OUT)
        RPi.GPIO.setup(self.LED_B, RPi.GPIO.OUT)
        RPi.GPIO.setup(self.LED_C, RPi.GPIO.OUT)
        RPi.GPIO.setup(self.LED_D, RPi.GPIO.OUT)
        RPi.GPIO.setup(self.LED_E, RPi.GPIO.OUT)
        RPi.GPIO.setup(self.LED_F, RPi.GPIO.OUT)
        RPi.GPIO.setup(self.LED_G, RPi.GPIO.OUT)
        RPi.GPIO.setup(self.LED_DP, RPi.GPIO.OUT)
        RPi.GPIO.setup(self.DIGIT1, RPi.GPIO.OUT)
        RPi.GPIO.setup(self.DIGIT2, RPi.GPIO.OUT)
        RPi.GPIO.setup(self.DIGIT3, RPi.GPIO.OUT)
        RPi.GPIO.setup(self.DIGIT4, RPi.GPIO.OUT)
    
        RPi.GPIO.output(self.DIGIT1, True)
        RPi.GPIO.output(self.DIGIT2, True)
        RPi.GPIO.output(self.DIGIT3, True)
        RPi.GPIO.output(self.DIGIT4, True)
    
        RPi.GPIO.setup(btn, RPi.GPIO.IN, pull_up_down=RPi.GPIO.PUD_UP)

    def showDigit(self, no, num, showDotPoint):
        """
        指定no(1-4)号数码管显示数字num(0-9)，第三个参数是显示不显示小数点（true/false）
        :param no:
        :param num:
        :param showDotPoint:
        :return:
        """
        # 先将正极拉低，关掉显示
        RPi.GPIO.output(self.DIGIT1, False)
        RPi.GPIO.output(self.DIGIT2, False)
        RPi.GPIO.output(self.DIGIT3, False)
        RPi.GPIO.output(self.DIGIT4, False)

        if num == 0:
            RPi.GPIO.output(self.LED_A, False)
            RPi.GPIO.output(self.LED_B, False)
            RPi.GPIO.output(self.LED_C, False)
            RPi.GPIO.output(self.LED_D, False)
            RPi.GPIO.output(self.LED_E, False)
            RPi.GPIO.output(self.LED_F, False)
            RPi.GPIO.output(self.LED_G, True)
            RPi.GPIO.output(self.LED_DP, not showDotPoint)
        elif num == 1:
            RPi.GPIO.output(self.LED_A, True)
            RPi.GPIO.output(self.LED_B, False)
            RPi.GPIO.output(self.LED_C, False)
            RPi.GPIO.output(self.LED_D, True)
            RPi.GPIO.output(self.LED_E, True)
            RPi.GPIO.output(self.LED_F, True)
            RPi.GPIO.output(self.LED_G, True)
            RPi.GPIO.output(self.LED_DP, not showDotPoint)
        elif num == 2:
            RPi.GPIO.output(self.LED_A, False)
            RPi.GPIO.output(self.LED_B, False)
            RPi.GPIO.output(self.LED_C, True)
            RPi.GPIO.output(self.LED_D, False)
            RPi.GPIO.output(self.LED_E, False)
            RPi.GPIO.output(self.LED_F, True)
            RPi.GPIO.output(self.LED_G, False)
            RPi.GPIO.output(self.LED_DP, not showDotPoint)
        elif num == 3:
            RPi.GPIO.output(self.LED_A, False)
            RPi.GPIO.output(self.LED_B, False)
            RPi.GPIO.output(self.LED_C, False)
            RPi.GPIO.output(self.LED_D, False)
            RPi.GPIO.output(self.LED_E, True)
            RPi.GPIO.output(self.LED_F, True)
            RPi.GPIO.output(self.LED_G, False)
            RPi.GPIO.output(self.LED_DP, not showDotPoint)
        elif num == 4:
            RPi.GPIO.output(self.LED_A, True)
            RPi.GPIO.output(self.LED_B, False)
            RPi.GPIO.output(self.LED_C, False)
            RPi.GPIO.output(self.LED_D, True)
            RPi.GPIO.output(self.LED_E, True)
            RPi.GPIO.output(self.LED_F, False)
            RPi.GPIO.output(self.LED_G, False)
            RPi.GPIO.output(self.LED_DP, not showDotPoint)
        elif num == 5:
            RPi.GPIO.output(self.LED_A, False)
            RPi.GPIO.output(self.LED_B, True)
            RPi.GPIO.output(self.LED_C, False)
            RPi.GPIO.output(self.LED_D, False)
            RPi.GPIO.output(self.LED_E, True)
            RPi.GPIO.output(self.LED_F, False)
            RPi.GPIO.output(self.LED_G, False)
            RPi.GPIO.output(self.LED_DP, not showDotPoint)
        elif num == 6:
            RPi.GPIO.output(self.LED_A, False)
            RPi.GPIO.output(self.LED_B, True)
            RPi.GPIO.output(self.LED_C, False)
            RPi.GPIO.output(self.LED_D, False)
            RPi.GPIO.output(self.LED_E, False)
            RPi.GPIO.output(self.LED_F, False)
            RPi.GPIO.output(self.LED_G, False)
            RPi.GPIO.output(self.LED_DP, not showDotPoint)
        elif num == 7:
            RPi.GPIO.output(self.LED_A, False)
            RPi.GPIO.output(self.LED_B, False)
            RPi.GPIO.output(self.LED_C, False)
            RPi.GPIO.output(self.LED_D, True)
            RPi.GPIO.output(self.LED_E, True)
            RPi.GPIO.output(self.LED_F, True)
            RPi.GPIO.output(self.LED_G, True)
            RPi.GPIO.output(self.LED_DP, not showDotPoint)
        elif num == 8:
            RPi.GPIO.output(self.LED_A, False)
            RPi.GPIO.output(self.LED_B, False)
            RPi.GPIO.output(self.LED_C, False)
            RPi.GPIO.output(self.LED_D, False)
            RPi.GPIO.output(self.LED_E, False)
            RPi.GPIO.output(self.LED_F, False)
            RPi.GPIO.output(self.LED_G, False)
            RPi.GPIO.output(self.LED_DP, not showDotPoint)
        elif num == 9:
            RPi.GPIO.output(self.LED_A, False)
            RPi.GPIO.output(self.LED_B, False)
            RPi.GPIO.output(self.LED_C, False)
            RPi.GPIO.output(self.LED_D, False)
            RPi.GPIO.output(self.LED_E, True)
            RPi.GPIO.output(self.LED_F, False)
            RPi.GPIO.output(self.LED_G, False)
            RPi.GPIO.output(self.LED_DP, not showDotPoint)

        if no == 1:
            RPi.GPIO.output(self.DIGIT1, True)
        elif no == 2:
            RPi.GPIO.output(self.DIGIT2, True)
        elif no == 3:
            RPi.GPIO.output(self.DIGIT3, True)
        elif no == 4:
            RPi.GPIO.output(self.DIGIT4, True)

    def show_date(self):
        """

        :return:
        """
        try:
            t = 0.005
            while True:
                time.sleep(t)
                self.showDigit(1, int(time.strftime("%H", time.localtime(time.time()))) / 10, False)
                time.sleep(t)
                self.showDigit(2, int(time.strftime("%H", time.localtime(time.time()))) % 10, True)
                time.sleep(t)
                self.showDigit(3, int(time.strftime("%M", time.localtime(time.time()))) / 10, False)
                time.sleep(t)
                self.showDigit(4, int(time.strftime("%M", time.localtime(time.time()))) % 10, False)
        except KeyboardInterrupt:
            pass
        RPi.GPIO.cleanup()

    def show_time(self):
        """

        :return:
        """
        try:
            t = 0.005
            while True:
                time.sleep(t)
                self.showDigit(1, int(time.strftime("%m", time.localtime(time.time()))) / 10, False)
                time.sleep(t)
                self.showDigit(2, int(time.strftime("%m", time.localtime(time.time()))) % 10, True)
                time.sleep(t)
                self.showDigit(3, int(time.strftime("%d", time.localtime(time.time()))) / 10, False)
                time.sleep(t)
                self.showDigit(4, int(time.strftime("%d", time.localtime(time.time()))) % 10, False)

        except KeyboardInterrupt:
            pass
        RPi.GPIO.cleanup()

    def show_temperature(self, temperature, humidity):
        """

        :return:
        """
        try:
            htc_server = htu.HTU21D()
            t = 0.005
            while True:
                temperature = htc_server.readTemperatureData()
                humidity = htc_server.readHumidityData()
                print "当前温度：{0}, 湿度：{1}".format(temperature, humidity)
                time.sleep(t)
                self.showDigit(1, int(int(temperature) / 10), False)
                time.sleep(t)
                self.showDigit(2, int(int(temperature) % 10), True)
                time.sleep(t)
                self.showDigit(3, int(int(humidity) / 10), False)
                time.sleep(t)
                self.showDigit(4, int(int(humidity) % 10), False)
        except KeyboardInterrupt:
            pass
        RPi.GPIO.cleanup()
