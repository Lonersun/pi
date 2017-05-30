# -*- coding:utf-8 -*-
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex


class AesEncrypt(object):

    # def __init__(self, key):
    #     self.key = key
    #     self.mode = AES.MODE_CBC

    def aes_encrypt(self, data, aes_key):
        key=aes_key  #加密时使用的key，只能是长度16,24和32的字符串
        BS = AES.block_size
        pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
        cipher = AES.new(key)
        encrypted = cipher.encrypt(pad(data))  #aes加密
        return encrypted

    # def encrypt(self, text):
    #     """
    #     加密函数
    #     :param text:
    #     :return:
    #     """
    #     cryptor = AES.new(self.key, self.mode, b'0000000000000000')
    #     #这里密钥key 长度必须为16（AES-128）,
    #     #24（AES-192）,或者32 （AES-256）Bytes 长度
    #     #目前AES-128 足够目前使用
    #     length = 16
    #     count = len(text)
    #     if count < length:
    #         add = (length-count)
    #         #\0 backspace
    #         text = text + ('\0' * add)
    #     elif count > length:
    #         add = (length-(count % length))
    #         text = text + ('\0' * add)
    #     self.ciphertext = cryptor.encrypt(text)
    #     #因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
    #     #所以这里统一把加密后的字符串转化为16进制字符串
    #     return b2a_hex(self.ciphertext)
    #
    # def decrypt(self, text):
    #     """
    #     解密
    #     :param text:
    #     :return:
    #     """
    #     #cryptor = AES.new(self.key, self.mode, self.key)
    #     cryptor = AES.new(self.key, self.mode)
    #     plain_text = cryptor.decrypt(a2b_hex(text))
    #     return plain_text.rstrip('\0')

# if __name__ == '__main__':
#     aes_encrypt = AES_ENCRYPT()      #初始化密钥
#     customer_id = "3f500ac5-020d-3ce3-a2a2-51a59ddd606e"
#     e = aes_encrypt.encrypt(customer_id)
#     d = aes_encrypt.decrypt(e)
#     print customer_id
#     print e
#     print d