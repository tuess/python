import requests
import re
from bs4 import BeautifulSoup

def main():
    url="https://www.csdn.net/"
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
    req=requests.get(url,headers)
    data=req.text
    bf=BeautifulSoup(data,'html.parser')
    for link in bf.find_all('a'):
        print(link.get('href'))
    
main()
