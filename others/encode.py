# -*- coding: utf-8 -*-
import base64
from Crypto.Cipher import AES

AES_SECRET_KEY = '625202f9149maomi' #此处16|24|32个字符

IV = "5efd3f6060emaomi"

# padding算法
BS = len(AES_SECRET_KEY)
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-ord(s[-1])]


class AES_ENCRYPT(object):
    def __init__(self):
        self.key = AES_SECRET_KEY
        self.mode = AES.MODE_CBC

    #加密函数
    def encrypt(self, text):

        cryptor = AES.new(self.key, self.mode,IV)
        self.ciphertext = cryptor.encrypt(pad(text))
        #AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题，使用base64编码
        return base64.b64encode(self.ciphertext)

    #解密函数
    def decrypt(self, text):
        decode = base64.b64decode(text)
        cryptor = AES.new(self.key, self.mode,IV)
        plain_text = cryptor.decrypt(decode)
        return plain_text

if __name__ == '__main__':
    aes_encrypt = AES_ENCRYPT()
    #text = "python 加密"
    #e = aes_encrypt.encrypt(text)
    e="1db1a91e265dfe30bb202816b22352f6"
    d = aes_encrypt.decrypt(e)
    print(text)
    print(e)
    print(d)
