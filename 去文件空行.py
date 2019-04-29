def main():
    infile=open("blank.txt")
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
main()
