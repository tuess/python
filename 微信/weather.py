# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import schedule,time,threading

def a():  
    url='http://www.weather.com.cn/weather1d/101200102.shtml'
    a=requests.get(url).text.encode('latin1').decode('utf-8')
    soup=BeautifulSoup(a,'html.parser')
    today=soup.find_all('p',class_='tem')
    high=today[0].span.string+today[0].em.string
    low=today[1].span.string+today[1].em.string
    w=soup.find_all('p',class_='win')
    level=w[0].span.string
    wea=soup.find_all('p',class_='wea')
    weather=wea[0].get_text()
    sunshine=soup.find_all('li',class_='li1 hot')
    sun=sunshine[0].span.string
    airpollution=soup.find_all('li',class_='li6 hot')
    air=airpollution[0].span.string
    clothes=soup.find_all('li',class_='li3 hot')
    cloth=clothes[0].span.string+','+clothes[0].p.string
    return weather,high,low,level,sun,air,cloth
def out():
    b=a()
    c='今天的天气是：'+b[0]+'\n'+'今天最高气温是：'+b[1]+'\n'+'今天最低气温是：'+b[2]+'\n'+'今天的风力大小为：'+b[3]+'\n'+'今天紫外线强度是：'+b[4]+'\n'+'今天空气污染指数是：'+b[5]+'\n'+'今天的穿衣指数是：'+b[6]+'\n'
    if b[0]=='晴':
        c+='今天是大号晴天，小仙女要记得防晒哦'
    elif b[0]=='多云':
        c+='今天多云，是个学习的好天气哦，小仙女不要偷懒哦'
    elif b[0]=='阴':
        c+='今天是阴天，小仙女要努力学习哦，要出门的话，记得带伞哦'
    elif b[0]=='雨':
        c+='今天是雨天，记得穿适合下雨天穿的鞋子哦'
    elif b[0]=='霾':
        c+='今天空气不太好，小仙女最好不要出门哦，出门的话也要带口罩哦'
    print(c)
    timer=threading.Timer(3,out)
    timer.start()

