#!/usr/bin/python
# -*- coding: utf-8 -*-
def main():
    n=int(input("输入你有多少个数字要比较"))
    max=float(input("输入一个数"))
    for i in range(n-1):
        i=float(input("输入一个数"))
        if i>max:
            max=i
    print("最大值是：",max)
main()
##x1,x2,x3=eval(input("输入三个数字"))
##print("最大的是：",max(x1,x2x,x3))
##只有eval能同时多项赋值
