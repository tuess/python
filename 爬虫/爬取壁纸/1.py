# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests,sys,random,time,os

def main():
    url_all_tmp=[]
    isExists=os.path.exists('./img')
    if not isExists:
        os.mkdir('./img')        
    url='http://www.dalibox.com/photo/show?id=991355'
    headers={'User-Agent':'Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3872.0 Mobile Safari/537.36'}
    response = requests.get(url,headers).text
##    print(response)
    div_all=BeautifulSoup(response,'lxml')
    div_tmp=div_all.find_all('img')
    print('共有'+str(len(div_tmp))+'张')
    for each in div_tmp:
##        print(each.get('data-avaurl'))
        url_tmp=each.get('data-avaurl')[6:]
        url_true='https://cdn1.bdcache.com/'+url_tmp
        print(url_true)
        img=requests.get(url_true,headers).content
        with open('./img/'+url_tmp[10:]+'.jpg','wb') as f:
            f.write(img)
        print('成功写入一张')
        
main()
