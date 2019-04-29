# -*- coding: utf-8 -*-
import requests,json,time,random
from bs4 import BeautifulSoup

def main():
    for x in range(10,16): #加页码
        a=[]
        url='https://wall.alphacoders.com/by_resolution.php?w=1920&h=1080&lang=Chinese&page='+str(x)
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
                 'Cookie':'_gid=GA1.2.1358056092.1552906216; _ga=GA1.2.826921159.1552906216; __cfduid=d74f257ea847cf707d1740f9241f884cd1552906218; cookieconsent_status=allow; wa_session=j2d0gi7cofov1v4k4qmn61ia5p6uip4qp1vftj9ts5vmb2l1qaok7j9qo1eqd6ijdhjh1njad5shco2tk0jm91mpdtupnj0eb764ao3'}
        req=requests.get(url,headers)
        sp=BeautifulSoup(req.text,'html.parser')
        for i in sp.find_all('img'): #找img标识的div
            a.append(i.get('data-src')) #在img里面找data-src
        del a[0:3] #前三个为None
        del a[1::2] #删掉偶数项的缩略图
        for each in a:
            each=each.replace('350','1920') #在url中把350改成1920
            target=str(each)
            a=requests.get(target,headers)
            b=a.content
            with open('./img2/'+str(each[-10:-4])+'.jpg','wb') as f: #切片找到图片id
                f.write(b)
        time.sleep(random.randint(5,30))
        
main()
