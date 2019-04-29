#!/usr/bin/python
# -*- coding: utf-8 -*-

from graphics import *

class Button:
    def __init__(self,win,center,width,height,label):
        w,h=width/2.0,height/2.0
        x,y=center.getX(),center.getY()
        self.xmin,self.xmax=x-w,x+w
        self.ymin,self.ymax=y-h,y+h
        p1=Point(self.xmin,self.ymin)
        p2=Point(self.xmax,self.ymax)
        self.rect=Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label=Text(center,label)
        self.label.draw(win)
        self.active()

    def clicked(self,p):
        return (self.active and
                self.xmin<=p.getX()<=self.xmax and
                self.ymin<=p.getY()<=self.ymax)

    def getLable(self):
        return self.label.getText()

    def active(self):
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active=True

    def deactive(self):
        self.label.setFill('gray')
        self.rect.setWidth(1)
        self.active=False
