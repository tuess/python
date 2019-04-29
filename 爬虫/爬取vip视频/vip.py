# -*- coding: utf-8 -*-
import requests
from urllib.request import quote,unquote

def main():
    a='都挺好'
    print(quote(a))
    url='http://so.iqiyi.com/so/q_'+str(a)
    b=requests.get(url).text
    print(b)

main()
