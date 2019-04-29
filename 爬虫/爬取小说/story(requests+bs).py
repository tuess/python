from bs4 import BeautifulSoup
import requests,sys
import random,time

class downloader(object):

    def __init__(self):
        self.server="http://www.biqukan.com"
        self.target="https://www.biqukan.com/0_319/" #小说的页面
        self.names=[] #存放章节名
        self.urls=[] #存放章节链接
        self.nums=0 #章节数

    def get_download_url(self): #获取下载链接
        req=requests.get(url=self.target)
        html=req.text
        div_bf=BeautifulSoup(html)
        div=div_bf.find_all('div',class_='listmain') #找到章节链接
        a_bf=BeautifulSoup(str(div[0]))
        a=a_bf.find_all('a') #提取链接
        self.nums=len(a[12:]) #切片删掉前12章最新章节
        for each in a[12:]:
            self.names.append(each.string) #向章节名列表中循环添加扎章节名
            self.urls.append(self.server+each.get('href')) #向链接列表中循环添加拼接好的链接

    def get_contents(self,target): #获取内容
        req=requests.get(url=target)
        html=req.text
        bf=BeautifulSoup(html)
        texts=bf.find_all('div',class_='showtxt') #获取章节内容(是一个列表)
        texts=texts[0].text.replace('\xa0'*8,'\n') #删除文中的空格和换行
        return texts

    def writein(self,name,path,text):
        write_flag=True
        with open(path,'a',encoding='utf-8') as f:
            f.write(name+'\n')
            f.writelines(text) #所以要用writelines方法
            f.write('\n')


if __name__== '__main__':
    dl=downloader()
    dl.get_download_url()
    print("《凡人修仙传·仙界篇》开始下载")
    for i in range(dl.nums):
        dl.writein(dl.names[i],"凡人修仙传·仙界篇.txt",dl.get_contents(dl.urls[i]))
        sys.stdout.write("  已下载：%.3f%%"%float(i/dl.nums)+'\r')
        sys.stdout.flush()
        time.sleep(random.randint(5,30))
    print("下载完成!")
