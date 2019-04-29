from bs4 import BeautifulSoup
import requests
def main():
    url="http://120.79.231.153/wordpress-4.9.4-zh_CN/wordpress/"
    strhtml=requests.get(url)
    soup=BeautifulSoup(strhtml.text,'lxml')
    data=soup.select('#wrapper>section.blog-section>div.container>div.row>div.col-md-8>article.post>header.entry-header>h3.entry-title>a')
    print(data)

main()
