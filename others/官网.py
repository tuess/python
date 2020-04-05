# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import base64
import random
import urllib.parse

def password():
     #添加头部信息
    my_headers=[{"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"},
                {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36"},
                {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0""Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14"},
                {"User-Agent":"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"}]
    header=random.choice(my_headers) #随机选取一个User-Agent
    #先请求，拿到cookie
    res=requests.get('http://221.233.24.27:8080/',headers=header)
    #print(res.cookies.get_dict())
    sessid=res.cookies.values()[0]
    print(sessid)
    cookies={'ASP.NET_SessionId':'mjqlwwjepes22bvfaz1omelk'}
    soup=BeautifulSoup(res.text,'html.parser')
    tag=soup.find_all('img')
    target='http://221.233.24.27:8080/verifycode.aspx'
    a=requests.get(target,headers=header)
    # 处理图片
    b=a.content
    with open('./1.jpg','wb') as f:
        f.write(b)
    checkcode=str(input('输入验证码：'))
    print(checkcode)
    payload={'__VIEWSTATE':'/wEPDwUJNDAzMzk1NDQ2D2QWAmYPZBYEAgUPFgIeBXN0eWxlBYABWi1JTkRFWDowO0JPUkRFUi1SSUdIVC1XSURUSDoxcHg7Qk9SREVSLUNPTExBUFNFOmNvbGxhcHNlO0JPUkRFUi1UT1AtV0lEVEg6MXB4O0ZPTlQtU0laRTo5cHQ7Qk9SREVSLUxFRlQtV0lEVEg6MXB4O2xlZnQ6MDt0b3A6MDsWAmYPZBYCAgIPZBYCZg8PZBYCHgdvbmNsaWNrBQ9yZXR1cm4gY2hlY2soKTtkAgcPFgQfAAUXWi1JTkRFWDowO3RvcDowO2xlZnQ6MDseB1Zpc2libGVoZGQY/3l0H3Cj7tA6FwG5ibInPkvXORksY2+yzV2opN22lg==',
             '__EVENTVALIDATION':'/wEWBgLBwvCqCwL/+tbVAgLHyfnnAgKd+7qdDgLcmtP7CgKY2YWXBhwejZli6Jf+XTd9v9O0ZKJv84LwriSEgFrNCct6j+MJ',
             'txtUid':'201661566',
             'btLogin':'%E7%99%BB%E5%BD%95',
             'txtPwd':'111',
             'selKind':'1',
             'txtCheckCode':'MC49'}
    req=requests.post('http://221.233.24.27:8080/',headers=header,data=payload,cookies=cookies)
    print(req.text)
    # with open('./1.jpg','rb') as d:
    #     base64_data=base64.b64encode(d.read())
    # data=urllib.parse.quote(base64_data)
    # print(len(data))
    
    # secret(data)
password()

def login():
    cookies=password()
    my_headers=[{"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"},
                {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36"},
                {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0""Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14"},
                {"User-Agent":"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"}]
    header=random.choice(my_headers) #随机选取一个User-Agent
    payload={'__VIEWSTATE':'/wEPDwUJNDAzMzk1NDQ2D2QWAmYPZBYEAgUPFgIeBXN0eWxlBYABWi1JTkRFWDowO0JPUkRFUi1SSUdIVC1XSURUSDoxcHg7Qk9SREVSLUNPTExBUFNFOmNvbGxhcHNlO0JPUkRFUi1UT1AtV0lEVEg6MXB4O0ZPTlQtU0laRTo5cHQ7Qk9SREVSLUxFRlQtV0lEVEg6MXB4O2xlZnQ6MDt0b3A6MDsWAmYPZBYCAgIPZBYCZg8PZBYCHgdvbmNsaWNrBQ9yZXR1cm4gY2hlY2soKTtkAgcPFgQfAAUXWi1JTkRFWDowO3RvcDowO2xlZnQ6MDseB1Zpc2libGVoZGQY/3l0H3Cj7tA6FwG5ibInPkvXORksY2+yzV2opN22lg==',
             '__EVENTVALIDATION':'/wEWBgLBwvCqCwL/+tbVAgLHyfnnAgKd+7qdDgLcmtP7CgKY2YWXBhwejZli6Jf+XTd9v9O0ZKJv84LwriSEgFrNCct6j+MJ',
             'txtUid':'201661566',
             'btLogin':'%E7%99%BB%E5%BD%95',
             'txtPwd':'111',
             'selKind':'1',
             'txtCheckCode':''}




def secret(target):
    token='https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=f17wDdwyaq3vTZGK8ntyKkGI&client_secret=7gqrnVQEEt8TDbEnDAC3SnyfVGcGHSra'
    a=requests.get(token).text
    b=eval(a)['access_token']
    url='https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token='+b
    headers={'Content-Type':'application/x-www-form-urlencoded'}
    payload={'url':target}
    res=requests.post(url,headers=headers,data=payload)
    print(res.text)
    
    

