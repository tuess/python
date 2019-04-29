import urllib.request
import urllib.parse
import random

def main():
    url="http://www.zzfriend.com/member.php?mod=logging&action=login&loginsubmit=yes&lssubmit=yes"
    postdata=urllib.parse.urlencode({
        "cookietime":"2592000",
        "formhash":"5051c399",
        "lostpwsubmit":"true",
        "password":"dtfxxx%404206",
        "username":"%CA%C0%CB%D7%B5%BD%CC%EC%C1%C1"        
        }).encode('utf-8') #添加表单数据并编码
    req=urllib.request.Request(url,postdata) #创建request对象
    #添加头部信息
    my_headers=["Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
                "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0""Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
                "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"]
    random1_header=random.choice(my_headers) #随机选取一个User-Agent    
    req.add_header('Uesr-Agent',random1_header)
    req.add_header("Referer","http://www.zzfriend.com/")
    req.add_header("Host","www.zzfriend.com")
    data=urllib.request.urlopen(req).read() #登录并爬取网页
    with open("antsociel.html","wb")as f:
        f.write(data)
##    url2="http://www.zzfriend.com/"
##    req2=urllib.request.Request(url,postdata)
##    req2.add_header('Uesr-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763')
##    data2=urllib.request.urlopen(req2).read()
##    with open("ant_social_home.html","wb") as d:
##        d.write(data2)
    
if __name__=="__main__":
    main()
        
