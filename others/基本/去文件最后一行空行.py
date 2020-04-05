def main():
    infile=open("blank.txt")
    outfile=open("noblank.txt","w")
    a=infile.readlines()
    for i in a:
        if i=="":
            break
        elif i=='\n':
            continue
        elif i==a[-1]:
            i=i[:-1]
            outfile.write(i)
        else:
            outfile.write(i)
    infile.close()
    outfile.close()
main()
