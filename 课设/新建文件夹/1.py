def main():
    a=input("请输入a")
    b=input("请输入b")
    if int(a)>100 or int(b)>100:
        print("不合法")
        return main()
    elif int(a)<0 or int(b)<0:
        print("不合法")
        return main()
    else:
        print("合法")
main()
