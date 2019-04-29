import urllib.request
def main():
    url=("https://blog.csdn.net/mm782642353/article/details/88141299")
    headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763")
    opener=urllib.request.build_opener()
    opener.addheaders=[headers]
    data=opener.open(url).read()
    outfile=open("blog.html","wb")
    outfile.write(data)
    outfile.close()

main()
