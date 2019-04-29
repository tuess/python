def main():
    infile=open("test.txt")
    c=[]
    while True:
        a=infile.readline()
        if a!="":
            b=a.split()
            b.append(float(b[1])+float(b[2]))
            b.reverse()
            c.append(b)
        else:
            break
    infile.close
    x=input("请输入数字(1,降序 2，升序 3,返回上级)")
    if x=="1":
        c.sort()
        print(c)
        for line in c:
            print("姓名："+line[3]+'\t'+"语文："+line[2]+'\t'+"数学："+line[1]+'\t'
                  +"总分："+str(line[0]))
        return main()
    elif x=="2":
        c.sort(reverse=True)
        print(c)
        for line in c:
            print("姓名："+line[3]+'\t'+"语文："+line[2]+'\t'+"数学："+line[1]+'\t'
                  +"总分："+str(line[0]))
        return main()
    else:
        print("输入错误，请重新输入")
        return main()
    
main()
