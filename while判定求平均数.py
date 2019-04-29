#!/usr/bin/python
# -*- coding: utf-8 -*-
def main():
    total=0.0
    count=0
    xstr=input("输入一个数(回车求出平均数)")
    while xstr!="":
        x=float(xstr)#类型转换
        total=total+x
        count+=1
        xstr=input("输入一个数(回车求出平均数)")
    print("平均数为：",total/count)

main()
