#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
    
def show():
    infile=open("student.txt","r")
    while True:
        a=infile.readline()
        if a!="":
            b=a.split()#拆分
        else:
            break #格式化插入
        print("姓名：",b[0]+'\t'+"语文：",b[1]+'\t'+"数学：",b[2]+'\t')
    print('\n')
    infile.close()
    
def write():
    d=input("输入一行成绩,以空格分开各项(输入分数即可，不需要加上“分”)")
    if d=="exit":
        return main()
    try: #index超出（输入内容过少）的错误捕获
        tem=d.split() #拆分
        s=[tem[1],tem[2]] #取后两个分数
        realnum=list(map(float,s)) #转换成float
        if realnum[0]>100 or realnum[1]>100: #判断输入分数的范围
            print("请输入正确的分数!")
            return write()
        elif realnum[0]<0 or realnum[1]<0:
            print("请输入正确的分数!")
            return write()
    except IndexError:
        print("请输入完整的成绩!!!"+'\n')
        return write()
    checkfile=open("student.txt")
    while True:
        a=checkfile.readline()#判读重复
        if tem[0] in a:
            print("请不要输入重复的学生姓名!!!"+'\n')
            return write()
        else:
            if a!="":
                continue
            else:
                break
    infile=open("student.txt","a")
    infile.write("\n"+d)
    print("添加成功！"+'\n')
    infile.close()
    
def delete():
    d=str(input("输入要删除的名字"))
    if d=="exit":
        return main()
    infile=open("student.txt","r")
    a=infile.read()
    if d not in a: #如果没找到存在d的x，证明输入错误
        print("输入的名字不存在！！！"+'\n')
        infile.close()
        return main()
    infile=open("student.txt","r")
    b=infile.readlines()
    outfile=open("student.txt","w",encoding="GBK")
    for l in b:
        if d not in l:
            outfile.write(l) #遇到输入的名字，跳过不写入
        else:
            continue
    print("删除成功！"+'\n')
    infile.close()
    outfile.close()
    
def search():
    d=str(input("输入要查找的信息（姓名，分数都可以）"))
    if d=="exit":
        return main()
    infile=open("student.txt","r")
    a=infile.readlines() #模糊查询
    for l in a:
        if d in l:
            s=l.split() #格式化插入
            print("姓名：",s[0]+'\t'+"语文：",s[1]+'\t'+"数学：",s[2]+'\t')
    print('\n')        
    infile.close()
 
def modify():
    d=str(input("输入要修改的名字"))
    if d=="exit":
        return main()
    infile=open("student.txt","r")
    outfile=open("test.txt","w",encoding="GBK")
    while True:
    #输入信息找到旧成绩
        a=infile.readline()
        if d in a:
            b=a.split()
            print("姓名：",b[0]+'\t'+"语文：",b[1]+'\t'+"数学：",b[2]+'\t')
            #输入新成绩替代旧成绩
            c=str(input("输入你要修改的语文成绩"))
            d=str(input("输入你要修改的数学成绩"))
            while c=="":
                if float(d)<0 or float(d)>100:
                    print("成绩错误，请重新输入")
                    return modify()
                else:
                    break
            while d=="":
                if float(c)<0 or float(d)>100:
                    print("成绩错误，请重新输入")
                    return modify()
                else:
                    break
            if c!="" and d!="": #利用切片来保存默认成绩，删除要修改的成绩
                del b[-1:-3:-1]
                b.append(c)
                b.append(d)
                f=' '.join(b)
                outfile.write(f+'\n')
                continue
            elif c=="" and d!="":
                del b[-1:-2:-1]
                b.append(d)
                f=' '.join(b)
                outfile.write(f+'\n')
                continue
            elif c!="" and d=="":
                del b[-2:-3:-1]
                b.insert(1,c)
                f=' '.join(b)
                outfile.write(f+'\n')
                continue
        elif a=="":
                break
        else:
            outfile.write(a)
            continue
    print("修改成功！"+'\n')
    infile.close()
    outfile.close()
    os.remove("student.txt")
    os.rename("test.txt","student.txt")

def sort():
    infile=open("student.txt")
    c=[]
    while True:
        a=infile.readline()
        if a!="":
            b=a.split()#拆分
            b.append(float(b[1])+float(b[2])) #把总分添加到列表的最后一项
            b.reverse() #倒置，方便下一步直接sort排序
            c.append(b)
        else:
            break
    infile.close
    x=input("请输入数字(1,升序 2，降序 3,返回上级)")
    if x=="1":
        c.sort() #升序
        for line in c:
            print("姓名："+line[3]+'\t'+"语文："+line[2]+'\t'+"数学："+line[1]+'\t'
                  +"总分："+str(line[0]))
        return sort()
    elif x=="2":
        c.sort(reverse=True) #降序
        for line in c:
            print("姓名："+line[3]+'\t'+"语文："+line[2]+'\t'+"数学："+line[1]+'\t'
                  +"总分："+str(line[0]))
        return sort()
    elif x=="3":
        return main()
    else:
        print("输入错误，请重新输入")
        return sort()

def noblank(): #去除文件最后一行的空白行
    infile=open("student.txt")
    outfile=open("test.txt","w",encoding="GBK")
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
    os.remove("student.txt")
    os.rename("test.txt","student.txt")

def noinblank(): #去掉文件中的空行
    infile=open("student.txt")
    outfile=open("test.txt","w")
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
    os.remove("student.txt")
    os.rename("test.txt","student.txt")

def main():
    print("学生成绩管理系统")
    print("1，查看成绩")
    print("2，增加成绩")
    print("3，删除成绩")
    print("4，查询成绩")
    print("5，修改成绩")
    print("6，成绩排序")
    print("7，退出")
    try: #误输入的捕获
        Operation=int(input("请输入数字进行操作"))
    except ValueError:
        print("请输入正确的数字!!!"+"\n")
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
        sort()
        mian()
    elif Operation == 7:
        exit()
    else:
        print("请输入正确的值!!!"+"\n")
        return main()
    
if __name__=='__main__':
    main()
