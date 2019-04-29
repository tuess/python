#!/usr/bin/python
# -*- coding: utf-8 -*-
class student:
    def __init__(self,name,hours,points):
        self.name=name
        self.hours=hours
        self.points=points

    def getname(self):
        return self.name

    def gethours(self):
        return self.hours

    def getpoints(self):
        return self.points

    def getgpa(self):
        return float(self.points)/float(self.hours)

def makeStudent(infostr):
    name,hours,points=infostr.split("\t")
    return student(name,hours,points)

def main():
    infile=open('text.txt','r')
    best=makeStudent(infile.readline())
    for line in infile:
        s=makeStudent(line)
        if s.getgpa()>best.getgpa():
            best=s
    infile.close()
    infile=open('text.txt','r')
    p=infile.read()
    print(p)

    print("最佳学生是：",best.getname())
    print("学时是：%s个学时"%best.gethours())
    print("绩点是：",best.getgpa())
    
if __name__ == '__main__':
    main()
