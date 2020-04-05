import requests

def cookie():
    #第一次访问response会setcookie，不确定时长
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.1021.400 QQBrowser/9.0.2524.400',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.8,en-us;q=0.6,en;q=0.5;q=0.4'}
    req=requests.get('https://plus.cdhand.com/web/index',headers=headers    )
    print(req.cookies.get_dict())
    print(req.text)

def score():
    url='https://plus.cdhand.com/index/web/check.html'
    payload={'xuehao':'201661566','mima':'111'}
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.1021.400 QQBrowser/9.0.2524.400'}
    cookies={'PHPSESSID':'dspqekg331ehl0t5mg794fva91',
             'UM_distinctid':'16ae4d17b473a5-01684829-7d4f5e27-1fa400-16ae4d17b489b0',
             'CNZZDATA1000542617':'1901923679-1558617096-https%253A%252F%252Fopen.weixin.qq.com%252F%7C1558617096'}
    req=requests.post(url=url,headers=headers,data=payload,cookies=cookies,verify=False)
    #print(req.cookies.get_dict())
    print(req.cookies.values())
    print(req.text)

def main():
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.1021.400 QQBrowser/9.0.2524.400'}
    s=requests.Session();
    res=s.get('https://plus.cdhand.com/web/index',headers=headers)
    print(res.headers)
    print(res.cookies.values())
    print(res.request.headers)

cookie();
#score();
#main();
#PHPSESSID,需要更新