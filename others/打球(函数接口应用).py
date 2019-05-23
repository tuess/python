#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import *
def main():
    a,b,n=getinputs()
    wina,winb=game(a,b,n)
    printEnd(wina,winb)

def getinputs():
    a=float(input("请输入a选手的胜率"))
    b=float(input("请输入b选手的胜率"))
    n=int(input("请输入游戏的局数"))
    return a,b,n

def game(a,b,n):
    wina=winb=0
    for i in range(n):
        scoreA,scoreB=onegame(a,b)
        if scoreA>scoreB:
            wina+=1
        else:
            winb+=1
    return wina,winb


def onegame(a,b):
    play="A"
    scoreA=scoreB=0
    while scoreA<=15 or scoreB<=15:
        if play=="A":
            if random()<a:
                scoreA+=1
            else:
                play="B"
        else:
            if random()<b:
                scoreB+=1
            else:
                play="A"
    return scoreA,scoreB

def printEnd(wina,winb):
    n=wina+winb
    print("总共进行了%d局游戏"%n)
    print("选手a赢了:{0}局，胜率为({1:0.1%})".format(wina,wina/n))
    print("选手b赢了:{0}局，胜率为({1:0.1%})".format(winb,winb/n))

if __name__ == '__main__':
    main()
