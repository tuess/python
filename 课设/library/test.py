#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
    
def show():
    infile=open("library.txt","r")
    while True:
        a=infile.readline()
        if a!="":
            b=a.split()#拆分
        else:
            break #格式化插入
        print("书名：",b[0]+'\t'+"作者：",b[1]+'\t'+"状态：",b[2]+'\t')
    print('\n')
    infile.close()
    
def write():
    d=input("输入书的信息(书名，作者，是否在馆)")
    if d=="exit":
        return main()
    b=d.split()
    checkfile=open("library.txt")
    while True:
        a=checkfile.readline()#判读重复
        if b[0] in a:
            print("请不要输入重复的书名!!!"+'\n')
            return write()
        else:
            if a!="":
                continue
            else:
                break
    checkfile.close()
    infile=open("library.txt","a")
    infile.write("\n"+d)
    print("添加成功！"+'\n')
    infile.close()
    
def delete():
    d=str(input("输入要删除的书名"))
    if d=="exit":
        return main()
    infile=open("library.txt","r")
    a=infile.read()
    if d not in a: #如果没找到存在的d，证明输入错误
        print("输入的书名不存在！！！"+'\n')
        infile.close()
        return main()
    infile=open("library.txt","r")
    b=infile.readlines()
    outfile=open("library.txt","w")
    for l in b:
        if d not in l:
            outfile.write(l) #遇到输入的书名，跳过不写入
        else:
            continue
    print("删除成功！"+'\n')
    infile.close()
    outfile.close()
    
def search():
    d=str(input("输入要查找的信息（书名，作者，状态都可以）"))
    if d=="exit":
        return main()
    infile=open("library.txt","r")
    a=infile.readlines() #模糊查询
    for l in a:
        if d in l:
            s=l.split() #格式化插入
            print("书名：",s[0]+'\t'+"作者：",s[1]+'\t'+"状态：",s[2]+'\t')
    print('\n')        
    infile.close()
 
def modify():
    d=str(input("输入要借阅的书名"))
    if d=="exit":
        return main()
    infile=open("library.txt","r")
    a=infile.read()
    if d not in a: #如果没找到存在的d，证明输入错误
        print("输入的书名不存在！！！"+'\n')
        infile.close()
        return main()
    infile=open("library.txt","r")
    outfile=open("text.txt","w")
    while True:
    #输入信息找到旧成绩
        a=infile.readline()
        if d in a:
            b=a.split()
            b[2]="借出"
            print("书名：",b[0]+'\t'+"作者：",b[1]+'\t'+"状态：",b[2]+'\t')
            f=" ".join(b)
            outfile.write(f+'\n')
            continue
        elif a=="":
            break
        else:
            outfile.write(a)
    print("借阅成功！"+'\n')
    infile.close()
    outfile.close()
    os.remove("library.txt")
    os.rename("text.txt","library.txt")
    
def modifyin():
    d=str(input("输入要还的书名"))
    if d=="exit":
        return main()
    infile=open("library.txt","r")
    a=infile.read()
    if d not in a: #如果没找到存在的d，证明输入错误
        print("输入的书名不存在！！！"+'\n')
        infile.close()
        return main()
    infile=open("library.txt","r")
    outfile=open("text.txt","w")
    while True:
    #输入信息找到旧成绩
        a=infile.readline()
        if d in a:
            b=a.split()
            b[2]="在馆"
            print("书名：",b[0]+'\t'+"作者：",b[1]+'\t'+"状态：",b[2]+'\t')
            f=" ".join(b)
            outfile.write(f+'\n')
            continue
        elif a=="":
            break
        else:
            outfile.write(a)
    print("还书成功！"+'\n')
    infile.close()
    outfile.close()
    os.remove("library.txt")
    os.rename("text.txt","library.txt")
    

def noblank(): #去除文件最后一行的空白行
    infile=open("library.txt")
    outfile=open("text.txt","w")
    a=infile.readlines()
    for i in a:
        if i=="":
            break
        elif i=='\n':
            continue
        elif i==a[-1]: #倒数第二个数据最后的\n
            i=i[:-1] #切片去掉\n
            outfile.write(i)
        else:
            outfile.write(i)
    infile.close()
    outfile.close()
    os.remove("library.txt")
    os.rename("text.txt","library.txt")

def noinblank(): #去掉文件中的空行
    infile=open("library.txt")
    outfile=open("text.txt","w")
    while True:
        line=infile.readline()
        if (line==""):
            break
        elif (line=='\n'): #等于\n跳过写入
            continue
        else:
            outfile.write(line)
    infile.close()
    outfile.close()
    os.remove("library.txt")
    os.rename("text.txt","library.txt")

def main():
    print("学生成绩管理系统")
    print("1，查看书籍")
    print("2，增加书籍")
    print("3，删除书籍")
    print("4，查询书籍")
    print("5，借阅书籍")
    print("6，归还书籍")
    print("7，退出")
    try: #误输入的捕获
        Operation=int(input("请输入数字进行操作"))
    except ValueError:
        print("请输入正确的序号!!!"+"\n")
        main()
    if Operation == 1:
        show()
        main()
    elif Operation == 2:
        write()
        noinblank()
        main()
    elif Operation == 3:
        delete()
        noblank()
        main()
    elif Operation == 4:
        search()
        main()
    elif Operation == 5:
        modify()
        noinblank()
        noblank()
        main()
    elif Operation == 6:
        modifyin()
        noinblank()
        noblank()
        main()
    elif Operation == 7:
        exit()
    else:
        print("请输入正确的值!!!"+"\n")
        return main()
    
if __name__=='__main__':
    main()
