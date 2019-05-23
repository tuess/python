# -*- coding: utf-8 -*-
import requests

def main():
    url='http://08imgmini.eastday.com/mobile/20190317/2019031712_8c73d47396a54eb9b93cd210237eefa5_0835_wmk.jpg'
    response = requests.get(url)
    img=response.content
    with open('1.jpg','wb') as f:
        f.write(img)

main()
