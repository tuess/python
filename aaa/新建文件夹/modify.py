import os
def main():
    infile=open("test.txt","r")
    outfile=open("1.txt","w")
    x=str(input("输入你要修改成绩的人的名字"))
    c=str(input("输入你要修改的语文成绩"))
    d=str(input("输入你要修改的数学成绩"))
    while True:
        a=infile.readline()
        if x in a:
            print(a)
            b=a.split()
            if c!="" and d!="":
                del b[-1:-3:-1]
                b.append(c)
                b.append(d)
                f=' '.join(b)
                outfile.write(f+'\n')
                continue
            elif c=="" and d!="":
                del b[-1:-2:-1]
                b.append(d)
                f=' '.join(b)
                outfile.write(f+'\n')
                continue
            elif c!="" and d=="":
                del b[-2:-3:-1]
                b.insert(1,c)
                f=' '.join(b)
                outfile.write(f+'\n')
                continue
        elif a=="":
                break
        else:
            outfile.write(a)
            continue
    infile.close()
    outfile.close()
    os.remove("test.txt")
    os.rename("1.txt","test.txt")

def no():
    infile=open("test.txt")
    outfile=open("noblank.txt","w")
    while True:
        line=infile.readline()
        if (line==""):
            break
        elif (line=='\n'):
            continue
        else:
            outfile.write(line)
    infile.close()
    outfile.close()
    os.remove("test.txt")
    os.rename("noblank.txt","test.txt")

def put():
    infile=open("test.txt")
    a=infile.read()
    print(a)
    infile.close()

put()   
main()
no()
