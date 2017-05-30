# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time


class Beep(object):

    def __init__(self, pin):
        self.pin = pin
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)

    def interval_beep(self, interval=0.5, frequency=1):
        """
        蜂鸣器鸣叫函数
        :param interval:
        :param frequency:
        :return:
        """
        while frequency:
            frequency -= 1
            GPIO.output(self.pin, GPIO.LOW)
            time.sleep(interval)
            GPIO.output(self.pin, GPIO.HIGH)
            time.sleep(interval)
        # 脚本运行完毕执行清理工作
        GPIO.cleanup()
