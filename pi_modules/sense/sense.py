# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time


class Sense(object):

    def __init__(self, pin):
        self.pin = pin
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT)

    def detct(self):
        """
        感应器侦测函数
        :return:
        """
        # 如果感应器针脚输出为True，则打印信息并执行蜂鸣器函数
        if GPIO.input(self.pin) == True:
            GPIO.cleanup()
            return True
        else:
            GPIO.cleanup()
            return False
