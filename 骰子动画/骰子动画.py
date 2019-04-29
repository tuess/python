#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import randrange
from graphics import *
from button import *
from dieview import *

def main():
    #创造窗口
    win=GraphWin("掷骰子")
    win.setCoords(0,0,10,10)
    win.setBackground("gray")

    #画出骰子和按钮
    die1=DieView(win,Point(3,7),2)
    die2=DieView(win,Point(7,7),2)
    rollButton=Button(win,Point(5,4.5),6,1,"投掷按钮")
    rollButton.active
    quitButton=Button(win,Point(5,1),2,1,"退出")
    quitButton.deactive

    #点击按钮投掷
    pt=win.getMouse()
    while not quitButton.clicked(pt):
        if rollButton.clicked(pt):
            value1=randrange(1,7)
            die1.setValue(value1)
            value2=randrange(1,7)
            die2.setValue(value1)
            quitButton.active
        pt=win.getMouse()
    win.close()

if __name__ == '__main__':
    main()
