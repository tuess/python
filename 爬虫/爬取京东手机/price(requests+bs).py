# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests,re,time,random

def shouji():
    phonename=dict()
    for i in range(1,129): #采集到第三页
        url='https://list.jd.com/list.html?cat=9987,653,655&ev=exprice%5FM2800L4499&page='+str(i)+'&sort=sort%5Frank%5Fasc&trans=1&JL=6_0_0&ms=6#J_main'
        url_session=requests.Session() #用session保持登录
        req=url_session.get(url).text #获取网页源码
        soup=BeautifulSoup(req,'html.parser') #用parser解析网页
        #find_all是bs的库函数，可以通过 find_all() 方法的 attrs 参数定义一个字典参数来搜索包含特殊属性的tag
        phone_html=soup.find_all(name='div',attrs={'class':'p-name'}) #通过p-name属性找到存放手机信息的地方
        for each in phone_html:
            for link in each.find_all('a'):
                shouji_html=str(link.get('href')[14:-5]) #通过切片只取src中的商品id
                phonename[shouji_html]=link.get_text().strip() #通过字典key给value赋值，将手机id和手机信息组成一对字典
    print('已下载了%s 页'%i)
    return phonename

if __name__=='__main__':
    price=shouji()
    outfile=open("price.txt","w",encoding="utf-8")
    for num in price:
        #抓包获取到后台的json
        price_url = 'https://p.3.cn/prices/mgets?callback=jQuery6983933&type=1&area=1_72_2799_0&pdtk=&pduid=14995199449641080515414&pdpin=&pin=null&pdbp=0&skuIds=J_'+str(num)+'&ext=11000000&source=item-pc'
        url_session=requests.Session()
        price_req=url_session.get(price_url).text #加上session发到后台得到传过来的json数据
        price_soup=re.findall(r'"p":"(.*?)"',price_req) #在json中用正则表达式找到"p"对应的价格
        for i in price_soup:
            shouji_data=price[num].encode('utf-8').decode('utf-8') #先将str转化为utf-8，再将utf-8转化为Unicode
            outfile.write(shouji_data+':'+str(i)+"元"+'\n')
        time.sleep(random.randint(5,30))
    outfile.close()
        
        
        
        
