# -*- coding: utf-8 -*-
import itchat,requests,time,threading
from bs4 import BeautifulSoup

def weather():
    url='http://www.weather.com.cn/weather1d/101200102.shtml'
    a=requests.get(url).text.encode('latin1').decode('utf-8')
    soup=BeautifulSoup(a,'html.parser')
    today=soup.find_all('p',class_='tem')
    high=today[0].span.string+today[0].em.string
    low=today[1].span.string+today[1].em.string
    w=soup.find_all('p',class_='win')
    wind=w[0].span['title']
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

def send():
    itchat.auto_login(hotReload=True,enableCmdQR = -1)
    a=weather()
    b='今天的天气是：'+a[0]+'\n'+'今天最高气温是：'+a[1]+'\n'+'今天最低气温是：'+a[2]+'\n'+'今天的风力大小为：'+a[3]+'\n'+'今天紫外线强度是：'+a[4]+'\n'+'今天空气污染指数是：'+a[5]+'\n'+'今天的穿衣指数是：'+a[6]+'\n'
    if a[0]=='晴':
        b+='今天是大号晴天，小仙女要记得防晒哦'
    elif a[0]=='多云':
        b+='今天多云，是个学习的好天气哦，小仙女不要偷懒哦'
    elif a[0]=='阴':
        b+='今天是阴天，小仙女要努力学习哦，要出门的话，记得带伞哦'
    elif a[0]=='雨':
        b+='今天是雨天，记得穿适合下雨天穿的鞋子哦'
    elif a[0]=='霾':
        b+='今天空气不太好，小仙女最好不要出门哦，出门的话也要带口罩哦'
    itchat.send(b,'poppet')
    itchat.send('发送成功','世俗到天亮')
    timer=threading.Timer(30,send)
    timer.start()

if __name__=='__main__':
    send()
