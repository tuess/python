#!/usr/bin/python
# -*- coding: utf-8 -*-

from graphics import *

class DieView:
    def __init__(self,win,center,size):
        self.win=win
        self.background="white"
        self.foreground="black"
        self.psize=0.1*size
        hsize=size/2.0
        offset=0.6*hsize
        #骰子的外观
        cx,cy=center.getX(),center.getY()
        p1=Point(cx-hsize,cy-hsize)
        p2=Point(cx+hsize,cy+hsize)
        rect=Rectangle(p1,p2)
        rect.draw(win)
        rect.setFill(self.background)
        #骰子上的七个圆圈(一个列表)
        self.pips=[self.__makePip(cx-offset,cy-offset),
                   self.__makePip(cx-offset,cy),
                   self.__makePip(cx-offset,cy+offset),
                   self.__makePip(cx,cy),
                   self.__makePip(cx+offset,cy-offset),
                   self.__makePip(cx+offset,cy),
                   self.__makePip(cx+offset,cy+offset)]
        #创建一个列表对应每个圈的控制
        self.onTable=[[],[3],[2,4],[2,3,4],[0,2,4,6],[0,2,3,4,6],[0,1,2,4,5,6]]
        self.setValue(1)

    def __makePip(self,x,y):
        pip=Circle(Point(x,y),self.psize)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        return pip

    def setValue(self,value):
        for pip in self.pips:
            pip.setFill(self.background)

        for i in self.onTable[value]:
            self.pips[i].setFill(self.foreground)
        
