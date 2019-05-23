import urllib.request
def use_proxy(addr,url):
    proxy=urllib.request.ProxyHandler({'http':addr})
    opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data=urllib.request.urlopen(url).read.decode("utf-8")
    return data
def main():
    addr="110.52.235.124:9999"
    data=use_proxy(addr,"http://www.baidu.com")
    print(len(data))

main()
