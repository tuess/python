from lxml import etree
import requests

def main():
    req=requests.get('https://www.bilibili.com/')
    html=etree.HTML(req.text)
    title=html.xpath('//*[@id="primary_menu"]/ul/li/a/div')
    print(title[0].text)
##    for each in title:
##        print(each[0].text)

main()
