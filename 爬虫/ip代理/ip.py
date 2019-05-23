import requests
import ssl
import lxml
import random
from bs4 import BeautifulSoup

def main():
    #获取当前访问使用的IP地址网站
    url="https://www.ipip.net/"

     #添加头部信息
    my_headers=[{"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"},
                {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36"},
                {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0""Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14"},
                {"User-Agent":"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"}]
    header=random.choice(my_headers) #随机选取一个User-Agent
    
    #设置代理，从代理网站上找出一个可用的代理IP
    proxies=[{'http':'121.69.37.6:9797'},{'http':'113.109.54.5:8118'}] #此处也可以通过列表形式，设置多个代理IP，后面通过random.choice()随机选取一个进行使用
    #随机选取一个代理ip
    proxy=random.choice(proxies)
    
    #使用代理IP进行访问
    res=requests.get(url,headers=header,proxies=proxy,timeout=10,verify=False)
    status=res.status_code # 状态码
    print(status)
    soup=BeautifulSoup(res.text,'html.parser')
    tag=soup.find_all(attrs={"style":"width: 20%"})
    print("ip地址为："+tag[0].a.string)

if __name__== '__main__':
    main();
