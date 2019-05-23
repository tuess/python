#!/usr/bin/python
# -*- coding: utf-8 -*-
def main():
    n=int(input("总共有多少个数字"))
    total=0.0
    for i in range(n):
        i=float(input("请输入一个数"))
        total=total+i
    print("平均数是：",total/n)
main()    
