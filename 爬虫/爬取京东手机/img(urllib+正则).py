# -*- coding: utf-8 -*-
import re
import urllib.request
import time,random

def pa(url,page):
    html1=urllib.request.urlopen(url).read() #网页代码读取出来
    html1=str(html1) #转换成str类型
    pat1='<div id="plist".+? <div class="page clearfix">'
    result1=re.compile(pat1).findall(html1) #从图片的开头匹配到结束,把需要的图片信息过滤出来
    pat2='<img width="220" height="220" data-img="1" src="//(.+?\.jpg)">'
    imagelist=re.compile(pat2).findall(result1[0]) #从各项li列表中匹配到图片链接
    x=1
    for imageurl in imagelist:
        imagename="./img/"+"第"+str(page)+"页 第"+str(x)+"张"+".jpg" #存放地址，文件名
        imageurl="http://"+imageurl #加上http,拼接链接
        try: #异常捕获，出错就跳过这一张
            urllib.request.urlretrieve(imageurl,filename=imagename) #用retrieve方法保存图片
        except urllib.error.URLError as e:
            if hasattr(e,"code"): #hasattr() 函数用于判断对象是否包含对应的属性,hasattr() 函数用于判断对象是否包含对应的属性
                x+=1
            if hasattr(e,"reason"):
                x+=1
        x+=1

for i in range(1,129):
    url="https://list.jd.com/list.html?cat=9987,653,655&page="+str(i)
    pa(url,i)
    print("已下载了%d 页"%(i))
    time.sleep(random.randint(5,30))
print("下载完成")
    
    
