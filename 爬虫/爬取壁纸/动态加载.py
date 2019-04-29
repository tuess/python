# -*- coding: utf-8 -*-
import requests,json,time，random
from contextlib import closing

def main():
    json_url="https://unsplash.com/napi/photos?page=1"
    photo_url='https://unsplash.com/photos/aaa/download'
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
             'Referer':'https://unsplash.com/'}
    req=requests.get(json_url,headers)
    html=json.loads(req.text)
    for i in html:
        target=photo_url.replace('aaa',str(i['id']))
        a=requests.get(target,stream=True,headers = headers)
        b=a.content #二进制内容
        with open('./img/'+str(i['id'])+'.jpg','wb') as f:
            f.write(b)
        time.sleep(random.randint(5,30))

if __name__=='__main__':
    main()
