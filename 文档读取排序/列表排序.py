#!/usr/bin/python
# -*- coding: utf-8 -*-
from studentscore import *

def read(filename):
    infile=open(filename,'r')
    students=[]
    for line in infile:
        students.append(makeStudent(line))
    infile.close()
    return students

def write(students,filename):
    outfile=open(filename,'w')
    for s in students:
        print("{0}\t{1}\t{2}\t".format(s.getname(),s.gethours(),s.getpoints()),
              file=outfile)
    outfile.close()

def main():
    filename=("test.txt")
    data=read(filename)
    data.sort(key=student.getgpa)
    filename=input("输入处理好的文件名：")
    write(data,filename)

if __name__=='__main__':
    main()
    
