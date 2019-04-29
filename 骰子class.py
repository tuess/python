#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import randrange
class die:
    def __init__(self,sides):
        self.sides=sides
        self.value=1
        
    def roll(self):
        self.value=randrange(1,self.sides+1)

    def getvalue(self):
        return self.value

    def setvalue(self,value):
        self.value=value
