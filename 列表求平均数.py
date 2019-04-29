#!/usr/bin/python
# -*- coding: utf-8 -*-
from math import sqrt

def getNumbers():
    num=[]
    xstr=input("请输入数字")
    while xstr!="":
        x=float(xstr)
        num.append(x)
        xstr=input("请输入数字")
    return num

def mean(num):
    total=0.0
    for n in num:
        total+=n
    return total/len(num)

def stdDev(num,xbar):
    sumDev=0.0
    for n in num:
        dev=n-xbar
        sumDev=sumDev+dev*dev
    return sqrt(sumDev/(len(num))-1)

def median(num):
    num.sort()
    size=len(num)
    mid=size//2
    if size%2 == 0:
        med=(num[mid]+num[mid-1])/2
    else:
        med=num[mid]
    return med

def main():
    data=getNumbers()
    xbar=mean(data)
    std=stdDev(data,xbar)
    med=median(data)

    print("平均数是：",xbar)
    print("中位数是：",med)
    print("标准差是：",std)

if __name__=='__main__':
    main()
