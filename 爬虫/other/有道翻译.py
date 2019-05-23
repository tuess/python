##import requests
##import json
##def get_date(word=None):
##    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc'
##    data = {
##        "type" : "AUTO",
##        "i" : word,
##        "doctype" : "json",
##        "xmlVersion" : "1.8",
##        "keyfrom" : "fanyi.web",
##        "ue" : "UTF-8",
##        "action" : "FY_BY_CLICKBUTTON",
##        "typoResult" : "true"
##    }
##    #请求表单数据
##    response=requests.post(url)
##    #将json格式字符串转字典
##    content=json.loads(response.text)
##    print(content['translateResult'][0][0]['tgt'])
##if __name__ == '__main__':
##    get_date("我爱倩倩")
##    
import os,urllib.request
import urllib.parse
import json
a = 5
while a > 0:
        txt = input('输入要翻译的内容!')
        if txt == '0':
                break
                
        else:
                url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom=https://www.baidu.com/link'

                data = {
                'from':'AUTO',
                'to':'AUTO',
                'smartresult':'dict',
                'client':'fanyideskweb',
                'salt':'1500092479607',
                'sign':'c98235a85b213d482b8e65f6b1065e26',
                'doctype':'json',
                'version':'2.1',
                'keyfrom':'fanyi.web',
                'action':'FY_BY_CL1CKBUTTON',
                'typoResult':'true'}

                data['i'] = txt

                data = urllib.parse.urlencode(data).encode('utf - 8')
                wy = urllib.request.urlopen(url,data)
                html = wy.read().decode('utf - 8')
                print(html)

                ta = json.loads(html)
                print('翻译结果: %s '% (ta['translateResult'][0][0]['tgt']))
                a = a - 1
                
