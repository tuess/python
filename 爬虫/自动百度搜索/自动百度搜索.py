import urllib.request
def main():
    keyword=str(input("请输入你要搜索的词："))
    keycode=urllib.request.quote(keyword)
    url="http://www.baidu.com/s?wd="+keycode
    reg=urllib.request.Request(url)
    data=urllib.request.urlopen(reg).read()
    outfile=open("baidu.html","wb")
    outfile.write(data)
    outfile.close()
main()
