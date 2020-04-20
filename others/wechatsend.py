#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from threading import Timer
from wxpy import *
import requests


#bot = Bot()
bot = Bot(console_qr=2,cache_path="botoo.pkl")
#bot = Bot(cache_path=True)

def get_news1():
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    contents = r.json()['content']
    translation= r.json()['translation']
    return contents,translation

def send_news():
    try:
        my_friend = bot.friends().search(u'寻梦')[0]    #你朋友的微信名称，不是备注，也不是微信帐号。
        my_friend.send(get_news1()[0])
        my_friend.send(get_news1()[1][5:])
        my_friend.send(u"来自你爸爸的心灵鸡汤！")
        t = Timer(1, send_news)
        t.start()
    except:
        my_friend = bot.friends().search('世俗到天亮')[0]
        my_friend.send(u"今天消息发送失败了")
        

    
if __name__ == "__main__":
    send_news()
